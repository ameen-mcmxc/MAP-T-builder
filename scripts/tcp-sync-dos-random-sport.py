#!/usr/bin/env python3

from scapy.all import *


conf.route6.add(dst='64:ff9b::/96',gw='2001:db8:6::1',dev='ens34')

def spoof_packet(packet):
    # check if the packet is a TCP packet
    if packet.haslayer(TCP) and packet[IPv6].src == "2001:db8:ce:11b:0:cb00:7108:1b":
        # extract the source port
        src_port = packet[TCP].sport

        print(f"TCP packet detected with source port {src_port}")
        spoofed_pkt = packet.copy()
        spoofed_pkt[TCP].sport = RandShort()
        # craft a new TCP packet
        sendp(spoofed_pkt, iface='ens34', inter=0.001, loop=1, verbose=0)

# Sniff for TCP packets on interface ens34 and call spoof_packet for each packet
sniff(iface="ens34", filter="tcp", prn=spoof_packet)
