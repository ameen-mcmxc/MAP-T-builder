#!/usr/bin/env python3

# This script is used to send UDP packet from the client to the Server.

from scapy.all import *

# Create the packet
ip = IP(dst="192.0.2.2")
udp = UDP(dport=80)
payload = load=("From IPv4 Cleint with Love")
pkt = ip/udp/payload

# Send the packet
send(pkt)
