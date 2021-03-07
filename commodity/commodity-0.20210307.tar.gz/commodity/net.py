# -*- coding:utf-8; tab-width:4; mode:python -*-

import socket

from .os_ import SubProcess, DEVNULL
from .type_ import checked_type
from .str_ import Printable
from .testing import Matcher


def is_port_open(port, proto='tcp', host=None):
    def localport():
        cmd = "ss --listening --numeric --{}  | grep ':{}'".format(proto, port)
        sp = SubProcess(cmd, shell=True, stdout=DEVNULL, stderr=DEVNULL)
        return sp.wait() == 0

    def remoteport():
        s = socket.socket()
        s.settimeout(1)
        try:
            s.connect((host, port))
            s.shutdown(socket.SHUT_RDWR)
            s.close()
            return True
        except socket.error:
            return False

    port = checked_type(int, port)
    host = checked_type((str, type(None)), host)

    if host in [None, 'localhost', '127.0.0.1']:
        return localport()

    assert proto == 'tcp', "proto %s not supported yet" % proto

    return remoteport()


def is_host_reachable(host):
    sp = SubProcess('ping -c 1 {0}'.format(host))
    return sp.wait() == 0


class Host(Printable):
    def __init__(self, name):
        self.name = checked_type(str, name)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return unicode(self.name)

localhost = Host('localhost')


class ListenPort(Matcher):
    def __init__(self, port, proto):
        self.port = checked_type(int, port)
        assert 0 < port < 65536
        self.proto = proto

    def _matches(self, item):
        self.host = checked_type(Host, item)
        return is_port_open(self.port, self.proto, self.host.name)

    def describe_to(self, description):
        description.append_text('listen at port {0}/{1}'.format(
                self.port, self.proto))


def listen_port(port, proto='tcp'):
    return ListenPort(port, proto)


class Reachable(Matcher):
    def _matches(self, host):
        self.host = checked_type(Host, host)
        return is_host_reachable(str(host))

    def describe_to(self, description):
        description.append_text("host is reachable")


def reachable():
    return Reachable()
