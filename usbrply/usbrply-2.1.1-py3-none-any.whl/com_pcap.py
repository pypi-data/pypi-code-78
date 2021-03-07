import sys
from .pcap_util import PcapParser, load_pcap


def default_arg(argsj, k, default):
    val = argsj.get(k)
    if val is None:
        return default
    else:
        return val


class PcapGen(object):
    def __init__(self, argsj):
        self.verbose = default_arg(argsj, "verbose", False)
        # JSON data objects buffered for next yield
        self.jbuff = None
        self.pcomments = None
        self.min_packet = default_arg(argsj, "min_packet", 0)
        self.max_packet = default_arg(argsj, "max_packet", float('inf'))
        self.cur_packn = None

        # XXX: don't think this is actually used, verify
        self.arg_fx2 = default_arg(argsj, "fx2", False)
        self.arg_device = default_arg(argsj, "device", None)
        # Default to device-hi if no other filtering is specified
        self.arg_device_hi = default_arg(
            argsj, "device_hi", self.arg_device is None
            and not argsj.get("vid") and not argsj.get("pid"))
        self.dev_drops = 0
        self.arg_setup = default_arg(argsj, "setup", False)
        self.arg_halt = default_arg(argsj, "halt", True)
        self.arg_remoteio = default_arg(argsj, "remoteio", False)
        self.arg_rel_pkt = default_arg(argsj, "rel_pkt", False)
        self.arg_print_short = default_arg(argsj, "print_short", False)
        self.arg_comment = default_arg(argsj, "comment", False)
        self.arg_packet_numbers = default_arg(argsj, "packet_numbers", True)

        # Either auto selected or user selected by now
        self.use_pcapng = "pcapng" in argsj["parser"]

    def gcomment(self, s):
        """Add global comment, not attached to a packet"""
        self.jbuff.append({'type': 'comment', 'v': s})

    def gwarning(self, s):
        self.gcomment("WARNING: " + str(s))

    def pcomment(self, s):
        """Add packet comment. Will be attached to the next packet"""
        self.pcomments.append(s)

    def pwarning(self, s):
        self.pcomment("WARNING: " + str(s))

    def printv(self, s):
        if self.verbose:
            print(s)

    def packnum(self):
        '''
        Originally I didn't print anything but found that it was better to keep the line numbers the same
        so that I could diff and then easier back annotate with packet numbers
        '''
        if self.arg_packet_numbers:
            postfix = "%s/%s" % (self.submit.packet_number, self.pktn_str())
        else:
            postfix = "N/A"
        self.pcomment("Generated from packet %s" % postfix)

    def packnumt(self):
        if self.arg_packet_numbers:
            return (self.submit.packet_number, self.pktn_str())
        else:
            return (None, None)

    def gen_data(self):
        parser = PcapParser(self.arg_fin, use_pcapng=self.use_pcapng)
        npackets = 0
        while True:
            npackets += 1
            if not parser.next(self.loop_cb):
                break

            if self.verbose:
                print("gen_data: %s new JSON entries" % (len(self.jbuff), ))

            # Pop packets
            for data in self.jbuff:
                if 0:
                    import json
                    print(data)
                    json.dumps(data)
                yield data
            self.jbuff = []

        if len(self.pending_complete) != 0:
            self.gwarning("%lu pending complete requests" %
                          (len(self.pending_complete)))
        # if len(self.pending_submit) != 0:
        #    self.gwarning("%lu pending submit requests" % (len(self.pending_submit)))

        self.gcomment("PcapGen: generated %u packets" % npackets)
        self.gcomment("PcapGen device filter: dropped %u / %u packets" %
                      (self.dev_drops, npackets))

        # Pop epilogue packets
        for p in self.jbuff:
            yield p
        self.jbuff = []

    def platform(self):
        assert 0, "required"

    def run(self):
        yield 'parser', self.parser()
        yield 'platform', self.platform()
        yield "fn", self.arg_fin
        yield 'args', sys.argv
        yield 'packet_min', self.min_packet
        yield 'packet_max', self.max_packet

        self.jbuff = []
        self.pcomments = []
        self.gcomment("Generated by usbrply")
        self.comment_source()
        self.gcomment("cmd: %s" % (' '.join(sys.argv), ))

        if self.arg_device_hi:
            self.arg_device = -1
            load_pcap(self.arg_fin,
                      self.loop_cb_devmax,
                      use_pcapng=self.use_pcapng)
            self.gcomment('PCapGen device hi: selected device %u' %
                          self.arg_device)
            self.cur_packn = 0

        self.printv("parsing from range %s to %s" %
                    (self.min_packet, self.max_packet))
        yield "data", self.gen_data()
