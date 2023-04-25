#!/usr/bin/env python3

# This script is used to send UDP packet from the client to the Server.

from scapy.all import *
import cryptography

# Create the packet
ip = IP(dst="192.0.2.2")
udp = UDP(dport=22)
payload = load=("I'm the payload of the UDP packet")
pkt = ip/udp/payload

# Send the packet
send(pkt)



## OR
# echo "Your message" | nc -u 192.0.2.2 22

## OR

# echo "Your message" | socat - UDP-DATAGRAM:192.0.2.2:22

## OR
# From specific source port: 5000

# hping3 -c 1 -2 -s 5000 -p 22 192.0.2.2
