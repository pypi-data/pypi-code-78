"""
Collection of NMEA helper methods which can be used
outside the NMEAMessage or NMEAReader classes

Created on 04 Mar 2021

:author: semuadmin
:copyright: SEMU Consulting © 2021
:license: BSD 3-Clause
"""

from datetime import datetime
from pynmeagps.nmeatypes_core import LA, LN
import pynmeagps.exceptions as nme


def int2hexstr(val: int) -> str:
    """
    Convert integer to hex string representation.

    :param int val: integer < 255 e.g. 31
    :return: hex representation of integer e.g. '1F'
    :rtype: str
    """

    return format(val, "02X")


def get_parts(message: object) -> tuple:
    """
    Get talker, msgid, payload and checksum of raw NMEA message.

    :param object message: entire message as bytes or string
    :return: tuple of (talker as str, msgID as str, payload as list, checksum as str)
    :rtype: tuple
    :raises: NMEAMessageError (if message is badly formed)
    """

    try:
        if isinstance(message, bytes):
            message = message.decode("utf-8")
        content, cksum = message.strip("$\r\n").split("*", 1)
        hdr, payload = content.split(",", 1)
        payload = payload.split(",")
        if hdr[0:1] == "G":  # standard
            talker = hdr[0:2]
            msgid = hdr[2:]
        else:
            talker = ""
            msgid = hdr
        return talker, msgid, payload, cksum
    except Exception as err:
        raise nme.NMEAMessageError(f"Badly formed message {message}") from err


def get_content(message: object) -> str:
    """
    Get content of raw NMEA message (everything between "$" and "*").

    :param object message: entire message as bytes or string
    :return: content as str
    :rtype: str
    """

    if isinstance(message, bytes):
        message = message.decode("utf-8")
    content, _ = message.strip("$\r\n").split("*", 1)
    return content


def list2csv(payload: list) -> str:
    """
    Convert list of strings to single string of comma separated values.

    :param list payload: list of values e.g. ["this", "that"]
    :return: string of comma separated values e.g. "this,that"
    :rtype: str
    """

    return ",".join(map(str, payload))


def calc_checksum(message: object) -> str:
    """
    Calculate checksum for raw NMEA message.

    :param object message: entire message as bytes or string
    :return: checksum as hex string
    :rtype: str
    """

    content = get_content(message)
    cksum = 0
    for sub in content:
        cksum ^= ord(sub)
    return int2hexstr(cksum)


def isvalid_cksum(message: object) -> bool:
    """
    Validate raw message checksum.

    :param bytes message: entire message as bytes or string
    :return: checksum valid flag
    :rtype: bool
    """

    _, _, _, cksum = get_parts(message)
    return cksum == calc_checksum(message)


def dmm2ddd(pos: str, att: str) -> float:
    """
    Convert NMEA lat/lon string to (unsigned) decimal degrees.

    :param str pos: (d)ddmm.mmmm
    :param str att: 'LA' (lat) or 'LN' (lon)
    :return: pos as decimal degrees
    :rtype: float

    """

    if pos == "" or att not in (LA, LN):
        return ""
    if att == LA:
        posdeg = float(pos[0:2])
        posmin = float(pos[2:])
    else:
        posdeg = float(pos[0:3])
        posmin = float(pos[3:])
    return round((posdeg + posmin / 60), 6)


def date2utc(dates: str) -> datetime.date:
    """
    Convert NMEA Date to UTC datetime.

    :param str times: NMEA date ddmmyy
    :return: UTC date YYyy:mm:dd
    :rtype: datetime.date
    """

    if dates == "":
        return ""
    utc = datetime.strptime(dates, "%d%m%y")
    return utc.date()


def time2utc(times: str) -> datetime.time:
    """
    Convert NMEA Date to UTC datetime.

    :param str times: NMEA time hhmmss.ss
    :return: UTC time hh:mm:ss.ss
    :rtype: datetime.time
    """

    if times == "":
        return ""
    # TODO not quite right should be decimal secs, not microsecs
    utc = datetime.strptime(times, "%H%M%S.%f")
    return utc.time()
