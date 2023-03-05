#!/usr/bin/env python3

# This script is used to send TCP packet from the client to the Server.

from scapy.all import *

ip = IP(dst="192.0.2.2")
tcp = TCP(dport=8)
data = "I am the payload of TCP packet"
pkt = ip/tcp/data

send(pkt)
