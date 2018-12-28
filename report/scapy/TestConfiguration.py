#! /usr/bin/env python
from scapy.all import *

def check_availability(target, label):
    print("\n--> ping to \"" + target + "\" (" + label + ")")
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
target = "192.168.40.11"
label = "R5"
check_availability(target, label)

target = "192.168.42.12"
label = "R5"
check_availability(target, label)

target = "192.168.42.1"
label = "R1"
check_availability(target, label)

target = "192.168.50.2"
label = "R1"
check_availability(target, label)

target = "192.168.44.3"
label = "R1"
check_availability(target, label)

target = "192.168.44.4"
label = "R2"
check_availability(target, label)

target = "192.168.55.5"
label = "R2"
check_availability(target, label)

target = "192.168.48.6"
label = "R2"
check_availability(target, label)

target = "192.168.50.7"
label = "R3"
check_availability(target, label)

target = "192.168.55.8"
label = "R3"
check_availability(target, label)

target = "192.168.48.9"
label = "R4"
check_availability(target, label)

target = "192.168.62.10"
label = "R4"
check_availability(target, label)

target = "192.168.40.50"
label = "PC1"
check_availability(target, label)

target = "192.168.62.60"
label = "PC2"
check_availability(target, label)

target = "192.168.62.70"
label = "XP1"
check_availability(target, label)

# Testing the NAT
target = "www.google.com"
label = "NAT"
check_availability(target, label)
