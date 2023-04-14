#!/usr/bin/env python3

from scapy.all import *

# Adding IPv6 route
#conf.route6.add(dst="64:ff9b::/96", gw="2001:db8:6::1")

# This scritp sniffes the communication channel on Interface ens34, looks for ICMPv6 packet.
# Then, it spoofes the source IP address of the found packet and sends identical packet to the same recipient.

# function to process the packet
def process_packet(packet):
    if packet.haslayer(ICMPv6EchoRequest) and packet[IPv6].src == "2001:db8:ce:11b:0:cb00:7108:1b":
        icmp_id = packet.getlayer(ICMPv6EchoRequest).id
        print("[+] Found ICMPv6 packet with source port (ICMP-ID): ", icmp_id)
        ether = Ether(dst="00:0c:29:e9:d1:1a", src="00:0c:29:b3:80:01")
        ipv6 = IPv6(src="2001:db8:ce:11b:0:cb00:7108:1b", dst="64:ff9b::c000:202")
        icmp6 = ICMPv6EchoRequest(id=icmp_id, data="From Ameen with Love!")
        new_packet = ether/ipv6/icmp6
        sendp(new_packet, iface="ens34")

# start sniffing on ens34
sniff(iface='ens34', filter="icmp6", prn=process_packet)
