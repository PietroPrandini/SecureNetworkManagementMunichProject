#! /usr/bin/env python
from scapy.all import *

packet1 = IP(dst="192.168.40.50", src="192.168.60.60") / ICMP(type=3, code=1)
packet2 = IP(dst="192.168.60.60", src="192.168.40.50") / ICMP(type=3, code=1)
send(packet1)
send(packet2)
