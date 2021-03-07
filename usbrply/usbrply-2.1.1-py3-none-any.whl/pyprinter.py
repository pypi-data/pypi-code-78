from __future__ import print_function
from usbrply import printer
from .printer import Printer, indented, indent_inc, indent_dec
import sys
import binascii
from . import usb
from .util import myord


def comment(s):
    indented('# %s' % (s, ))


def bytes2AnonArray(bytes_data):
    # In Python2 bytes_data is a string, in Python3 it's bytes.
    # The element type is different (string vs int) and we have to deal
    # with that when printing this number as hex.

    byte_str = "b\""

    for i in range(len(bytes_data)):
        if i and i % 16 == 0:
            byte_str += '\"\n            b\"'
        byte_str += "\\x%02X" % (myord(bytes_data[i]), )
    return byte_str + "\""


def printControlRequest(submit, data_str, data_size, pipe_str):
    if submit.m_ctrl.bRequestType & usb.URB_TRANSFER_IN:
        indented("buff = controlRead(0x%02X, 0x%02X, 0x%04X, 0x%04X, %u)" %
                 (submit.m_ctrl.bRequestType, submit.m_ctrl.bRequest,
                  submit.m_ctrl.wValue, submit.m_ctrl.wIndex, data_size))
    else:
        indented("controlWrite(0x%02X, 0x%02X, 0x%04X, 0x%04X, %s)" %
                 (submit.m_ctrl.bRequestType, submit.m_ctrl.bRequest,
                  submit.m_ctrl.wValue, submit.m_ctrl.wIndex, data_str))


class LibusbPyPrinter(Printer):
    def __init__(self, argsj, verbose=False):
        Printer.__init__(self, argsj)
        self.prevd = None
        self.wrapper = argsj.get("wrapper", False)
        self.sleep = argsj.get("sleep", False)
        self.packet_numbers = argsj.get("packet_numbers", True)
        # FIXME
        self.vid = 0
        self.pid = 0
        self.verbose = verbose

    def print_imports(self):
        print('''\
import binascii
import time
import usb1
''',
              file=printer.print_file)

    def print_wrapper_header(self):
        print('''\
def validate_read(expected, actual, msg):
    if expected != actual:
        print('Failed %s' % msg)
        print('  Expected; %s' % binascii.hexlify(expected,))
        print('  Actual:   %s' % binascii.hexlify(actual,))
        #raise Exception('failed validate: %s' % msg)

''',
              file=printer.print_file)
        print('def replay(dev):', file=printer.print_file)
        indent_inc()
        print('''\
    def bulkRead(endpoint, length, timeout=None):
        return dev.bulkRead(endpoint, length, timeout=(1000 if timeout is None else timeout))

    def bulkWrite(endpoint, data, timeout=None):
        dev.bulkWrite(endpoint, data, timeout=(1000 if timeout is None else timeout))
    
    def controlRead(bRequestType, bRequest, wValue, wIndex, wLength,
                    timeout=None):
        return dev.controlRead(bRequestType, bRequest, wValue, wIndex, wLength,
                    timeout=(1000 if timeout is None else timeout))

    def controlWrite(bRequestType, bRequest, wValue, wIndex, data,
                     timeout=None):
        dev.controlWrite(bRequestType, bRequest, wValue, wIndex, data,
                     timeout=(1000 if timeout is None else timeout))

    def interruptRead(endpoint, size, timeout=None):
        return dev.interruptRead(endpoint, size,
                    timeout=(1000 if timeout is None else timeout))

    def interruptWrite(endpoint, data, timeout=None):
        dev.interruptWrite(endpoint, data, timeout=(1000 if timeout is None else timeout))
''',
              file=printer.print_file)

    def header(self):
        comment("Generated by usbrply")
        # comment("Date: %s" % (UVDCurDateTime()))
        comment("cmd: %s" % (' '.join(sys.argv), ))
        indented("")

        if self.wrapper:
            self.print_imports()
            print("", file=printer.print_file)
            self.print_wrapper_header()

    def footer(self):
        if not self.wrapper:
            return
        print('''
def open_dev(usbcontext=None):
    if usbcontext is None:
        usbcontext = usb1.USBContext()
    
    print('Scanning for devices...')
    for udev in usbcontext.getDeviceList(skip_on_error=True):
        vid = udev.getVendorID()
        pid = udev.getProductID()
        if (vid, pid) == (''' + "0x%04X, 0x%04X" % (self.vid, self.pid) + '''):
            print("")
            print("")
            print('Found device')
            print('Bus %03i Device %03i: ID %04x:%04x' % (
                udev.getBusNumber(),
                udev.getDeviceAddress(),
                vid,
                pid))
            return udev.open()
    raise Exception("Failed to find a device")

if __name__ == "__main__":
    import argparse 
    
    parser = argparse.ArgumentParser(description='Replay captured USB packets')
    args = parser.parse_args()

    usbcontext = usb1.USBContext()
    dev = open_dev(usbcontext)
    dev.claimInterface(0)
    dev.resetDevice()
    replay(dev)

''',
              file=printer.print_file)

    def packet_number_str(self, d):
        if self.packet_numbers:
            return "packet %s/%s" % (d["submit"]["packn"],
                                     d["complete"]["packn"])
        else:
            # TODO: consider counting instead of by captured index
            return "packet"

    def parse_data(self, d):
        # print(d)
        if self.sleep and self.prevd and d["type"] != "comment":
            try:
                dt = d["submit"]["t"] - self.prevd["submit"]["t"]
            except KeyError:
                raise ValueError("Input JSON does not support timestamps")
            if dt >= 0.001:
                indented('time.sleep(%.3f)' % (dt, ))

        if d["type"] == "comment":
            comment(d["v"])
            return

        packet_numbering = self.packet_number_str(d)

        if "comments" in d:
            for c in d["comments"]:
                comment(c)

        if d["type"] == "controlRead":
            # Is it legal to have a 0 length control in?
            indented("buff = controlRead(0x%02X, 0x%02X, 0x%04X, 0x%04X, %u)" %
                     (d["bRequestType"], d["bRequest"], d["wValue"],
                      d["wIndex"], d["wLength"]))
            indented("validate_read(%s, buff, \"%s\")" % (bytes2AnonArray(
                binascii.unhexlify(d["data"])), packet_numbering))
        elif d["type"] == "controlWrite":
            data_str = bytes2AnonArray(binascii.unhexlify(d["data"]))
            indented("controlWrite(0x%02X, 0x%02X, 0x%04X, 0x%04X, %s)" %
                     (d["bRequestType"], d["bRequest"], d["wValue"],
                      d["wIndex"], data_str))

        elif d["type"] == "bulkRead":
            data_str = "\"\""
            indented("buff = bulkRead(0x%02X, 0x%04X)" % (d["endp"], d["len"]))
            indented("validate_read(%s, buff, \"%s\")" % (bytes2AnonArray(
                binascii.unhexlify(d["data"])), packet_numbering))
        elif d["type"] == "bulkWrite":
            # Note that its the submit from earlier, not the ack that we care about
            data_str = bytes2AnonArray(binascii.unhexlify(d["data"]))
            # def bulkWrite(self, endpoint, data, timeout=0):
            indented("bulkWrite(0x%02X, %s)" % (d["endp"], data_str))

        elif d["type"] == "interruptRead":
            data_str = "\"\""
            indented("buff = interruptRead(0x%02X, 0x%04X)" %
                     (d["endp"], d["len"]))
            indented("validate_read(%s, buff, \"%s\")" % (bytes2AnonArray(
                binascii.unhexlify(d["data"])), packet_numbering))

        elif d["type"] == "interruptWrite":
            indented("interruptWrite(0x%02X, %s)" % (d["endp"], data_str))
        else:
            if self.verbose:
                print("LibusbPyPrinter WARNING: dropping %s" % (d["type"], ))

        # these aren't event added to JSON right now
        # print('%s# WARNING: omitting interrupt' % (indent,))

        if d["type"] != "comment":
            self.prevd = d

    def run(self, jgen):
        self.header()

        # Last wire command (ie non-comment)
        # Used to optionally generate timing
        self.prevd = None

        # Convert generator into static JSON
        j = {}
        for k, v in jgen:
            j[k] = v

        for d in j["data"]:
            self.parse_data(d)

        self.footer()
