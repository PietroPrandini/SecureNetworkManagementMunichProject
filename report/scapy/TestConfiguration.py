#! /usr/bin/env python
from scapy.all import *

# Availability of each subnets
arping("192.168.40.0/24")
arping("192.168.42.0/24")
arping("192.168.44.0/24")
arping("192.168.48.0/24")
arping("192.168.50.0/24")
arping("192.168.55.0/24")
arping("192.168.62.0/24")
# Testing the NAT
arping("www.google.com")
