#!/usr/bin/env bash

# Availability of each device
ping -c 3 192.168.40.50

ping -c 3 192.168.40.11

ping -c 3 192.168.42.1

ping -c 3 192.168.42.12

ping -c 3 192.168.44.3

ping -c 3 192.168.44.4

ping -c 3 192.168.48.6

ping -c 3 192.168.48.9

ping -c 3 192.168.50.1

ping -c 3 192.168.50.7

ping -c 3 192.168.55.8

ping -c 3 192.168.55.5

ping -c 3 192.168.62.10

ping -c 3 192.168.62.60

ping -c 3 192.168.62.70

# Testing the NAT
ping -c 3 www.google.com
