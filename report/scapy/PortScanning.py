#! /usr/bin/env python
from scapy.all import *

packet = IP(dst="192.168.40.50") / TCP(dport=(1,1024), flags="S")
sr(packet, inter=0.005)
