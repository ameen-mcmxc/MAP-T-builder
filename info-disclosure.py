#!/usr/bin/env python3

from scapy.all import *


# This script prints out the payload content of the sniffed UDP or TCP Packet and also the data inside the ICMPv6 packet.
def packet_handler(packet):
        if UDP in packet:
            udp_payload = packet[UDP].payload
            print(f"UDP Packet:")
            print(f"Payload: {udp_payload}")
        elif ICMPv6EchoRequest in packet:
            icmp6_payload = packet[ICMPv6EchoRequest].data
            print(f"ICMPv6 Echo Request Packet:")
            print(f"Payload: {icmp6_payload}")
        elif TCP in packet:
            tcp_payload = packet[TCP].payload
            print(f"TCP Payload: {tcp_payload}")
sniff(iface='ens34', filter='udp or icmp6 or tcp', prn=packet_handler)
