#! /usr/bin/env python
from scapy.all import *

packet = IP(dst="192.168.40.0/24") / ICMP()
sr(packet, inter=0.010)
