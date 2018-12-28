#! /usr/bin/env python
from scapy.all import *

# Preparing the packet with no flags set
victim = "192.168.62.60"
packet_without_flags = IP(dst=victim)/TCP(flags="")

# Sending the packet
send(packet_without_flags)
