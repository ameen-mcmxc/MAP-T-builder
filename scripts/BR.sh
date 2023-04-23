#!/bin/bash

# Flush iptables rules
sudo iptables -F
sudo ip6tables -F

br_v6_int='ens34'
br_v6_ip='2001:db8:6::1/64'

br_v4_int='ens35'
br_v4_ip='192.0.2.1/24'

ce_v6_ip='2001:db8:6::11b'

ce_nat44_global_ip_net='203.0.113.0/24'


# Enable IP forwarding
echo 1 > /proc/sys/net/ipv4/ip_forward
echo 1 > /proc/sys/net/ipv6/conf/all/forwarding

ip link set $br_v6_int up
ip address add $br_v6_ip dev $br_v6_int

ip link set $br_v4_int up
ip address add $br_v4_ip dev $br_v4_int

ip route add 2001:db8:ce:11b::/64 via $ce_v6_ip
#ip route add 2001:db8:ce:774::/64 via 2001:db8:6::774

# Weiter Schrittee

/sbin/modprobe jool_mapt
jool_mapt instance add "BR" --netfilter --dmr 64:ff9b::/96
jool_mapt -i "BR" fmrt add 2001:db8:ce::/51 $ce_nat44_global_ip_net 13 0
jool_mapt -i "BR" global update map-t-type BR
