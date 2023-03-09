#!/usr/bin/env python3

from scapy.all import *

def packet_handler(packet):
    if packet.haslayer(ICMPv6EchoRequest):
        icmp_id = packet.getlayer(ICMPv6EchoRequest).id
        new_packet = Ether(dst="00:0c:29:e9:d1:1a", src="00:0c:29:b3:80:01")
        /IPv6(src="2001:db8:ce:11b:0:cb00:7108:1b", dst="64:ff9b::c000:202")/ICMPv6EchoRequest(id=icmp_id, data="Nastia")
        sendp(new_packet, iface="ens34")

sniff(iface="ens34", prn=packet_handler, filter="(ether proto 0x86dd) and (icmp6)")
