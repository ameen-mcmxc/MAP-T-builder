#!/bin/bash

/sbin/ip link set eth0 up
/sbin/ip address add 2001:db8:6::1/64 dev eth0

/sbin/ip link set eth1 up
/sbin/ip address add 203.0.113.1/24 dev eth1

/sbin/ip route add 2001:db8:ce:11b::/64 via 2001:db8:6::11b
/sbin/ip route add 2001:db8:ce:774::/64 via 2001:db8:6::774

/sbin/sysctl -w net.ipv4.conf.all.forwarding=1
/sbin/sysctl -w net.ipv6.conf.all.forwarding=1


# Weiter Schrittee

/sbin/modprobe jool_mapt
jool_mapt instance add "BR" --netfilter --dmr 64:ff9b::/96
jool_mapt -i "BR" fmrt add 2001:db8:ce::/51 192.0.2.0/24 13 0
jool_mapt -i "BR" global update map-t-type BR
