#! /usr/bin/env python
from scapy.all import *

# Availability of each device
target = "192.168.40.50"
ans,unans = arping(target)
if ans:
    print(target + ' is reachable, summary:')
    ans.summary()
else:
    print(target + ' is not reachable, summary:')
    unans.summary()

target = "192.168.40.11"
ans.summary()

target = "192.168.42.1"
ans,unans = arping(target)
if ans:
    print(target + ' is reachable, summary:')
    ans.summary()
else:
    print(target + ' is not reachable, summary:')
    unans.summary()

target = "192.168.42.12"
ans,unans = arping(target)
if ans:
    print(target + ' is reachable, summary:')
    ans.summary()
else:
    print(target + ' is not reachable, summary:')
    unans.summary()

target = "192.168.44.3"
ans,unans = arping(target)
if ans:
    print(target + ' is reachable, summary:')
    ans.summary()
else:
    print(target + ' is not reachable, summary:')
    unans.summary()

target = "192.168.44.4"
ans,unans = arping(target)
if ans:
    print(target + ' is reachable, summary:')
    ans.summary()
else:
    print(target + ' is not reachable, summary:')
    unans.summary()

target = "192.168.48.6"
ans,unans = arping(target)
if ans:
    print(target + ' is reachable, summary:')
    ans.summary()
else:
    print(target + ' is not reachable, summary:')
    unans.summary()

target = "192.168.48.9"
ans,unans = arping(target)
if ans:
    print(target + ' is reachable, summary:')
    ans.summary()
else:
    print(target + ' is not reachable, summary:')
    unans.summary()

target = "192.168.50.1"
ans,unans = arping(target)
if ans:
    print(target + ' is reachable, summary:')
    ans.summary()
else:
    print(target + ' is not reachable, summary:')
    unans.summary()

target = "192.168.50.7"
ans,unans = arping(target)
if ans:
    print(target + ' is reachable, summary:')
    ans.summary()
else:
    print(target + ' is not reachable, summary:')
    unans.summary()

target = "192.168.55.8"
ans,unans = arping(target)
if ans:
    print(target + ' is reachable, summary:')
    ans.summary()
else:
    print(target + ' is not reachable, summary:')
    unans.summary()

target = "192.168.55.5"
ans,unans = arping(target)
if ans:
    print(target + ' is reachable, summary:')
    ans.summary()
else:
    print(target + ' is not reachable, summary:')
    unans.summary()

target = "192.168.62.10"
ans,unans = arping(target)
if ans:
    print(target + ' is reachable, summary:')
    ans.summary()
else:
    print(target + ' is not reachable, summary:')
    unans.summary()

target = "192.168.62.60"
ans,unans = arping(target)
if ans:
    print(target + ' is reachable, summary:')
    ans.summary()
else:
    print(target + ' is not reachable, summary:')
    unans.summary()

target = "192.168.62.70"
ans,unans = arping(target)
if ans:
    print(target + ' is reachable, summary:')
    ans.summary()
else:
    print(target + ' is not reachable, summary:')
    unans.summary()

# Testing the NAT
arping("www.google.com")
ans,unans = arping(target)
if ans:
    print(target + ' is reachable, summary:')
    ans.summary()
else:
    print(target + ' is not reachable, summary:')
    unans.summary()
