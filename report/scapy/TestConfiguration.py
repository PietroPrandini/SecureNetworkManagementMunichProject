#! /usr/bin/env python
from scapy.all import *

# Availability of each device
ans,unans = arping("192.168.40.50")
ans.summary()
unans.summary()

ans,unans = arping("192.168.40.11")
ans.summary()
unans.summary()

ans,unans = arping("192.168.42.1")
ans.summary()
unans.summary()

ans,unans = arping("192.168.42.12")
ans.summary()
unans.summary()

ans,unans = arping("192.168.44.3")
ans.summary()
unans.summary()

ans,unans = arping("192.168.44.4")
ans.summary()
unans.summary()

ans,unans = arping("192.168.48.6")
ans.summary()
unans.summary()

ans,unans = arping("192.168.48.9")
ans.summary()
unans.summary()

ans,unans = arping("192.168.50.1")
ans.summary()
unans.summary()

ans,unans = arping("192.168.50.7")
ans.summary()
unans.summary()

ans,unans = arping("192.168.55.8")
ans.summary()
unans.summary()

ans,unans = arping("192.168.55.5")
ans.summary()
unans.summary()

ans,unans = arping("192.168.62.10")
ans.summary()
unans.summary()

ans,unans = arping("192.168.62.60")
ans.summary()
unans.summary()

ans,unans = arping("192.168.62.70")
ans.summary()
unans.summary()

# Testing the NAT
arping("www.google.com")
ans.summary()
unans.summary()
