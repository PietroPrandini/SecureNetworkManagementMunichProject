#!/usr/bin/env bash
# Routing to the NAT
route add -net 0.0.0.0/0 gw 192.168.40.11
# Adding nameservers
echo "nameserver 8.8.8.8" >> /etc/resolv.conf
echo "nameserver 8.8.4.4" >> /etc/resolv.conf
