#! /usr/bin/env python
from scapy.all import *

def check_availability(target):
    ans,unans = sr(IP(dst=target)/ICMP())
    if ans:
        print(target + ' is reachable, summary:')
        ans.summary()
        return ans,unans
    else:
        print(target + ' is not reachable, summary:')
        unans.summary()
        return ans,unans

# Availability of each device
target = "192.168.40.50"
check_availability(target)

target = "192.168.40.11"
check_availability(target)

target = "192.168.42.1"
check_availability(target)

target = "192.168.42.12"
check_availability(target)

target = "192.168.44.3"
check_availability(target)

target = "192.168.44.4"
check_availability(target)

target = "192.168.48.6"
check_availability(target)

target = "192.168.48.9"
check_availability(target)

target = "192.168.50.2"
check_availability(target)

target = "192.168.50.7"
check_availability(target)

target = "192.168.55.8"
check_availability(target)

target = "192.168.55.5"
check_availability(target)

target = "192.168.62.10"
check_availability(target)

target = "192.168.62.60"
check_availability(target)

target = "192.168.62.70"
check_availability(target)

# Testing the NAT
target = "www.google.com"
check_availability(target)
