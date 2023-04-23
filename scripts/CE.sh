#!/bin/bash

ce_local_int='ens34'
ce_global_int='ens35'
ce_local_ip='10.0.0.1/24'

ce_local_ip_net='10.0.0.0/24'
ce_global_ip='2001:db8:6::11b/64'
br_global_ip='2001:db8:6::1'

inside_napt_int='to_global'
inside_napt_ip='192.168.0.2/24'
inside_napt_ip_no_mask='192.168.0.2'

inside_global_int='to_napt'
inside_global_ip='192.168.0.1/24'
inside_global_ip_no_mask='192.168.0.1'

ports_set='55296-57343'
nat44_global_ip='203.0.113.8'
nat44_global_ip_net='203.0.113.0/24'

# Flush iptables rules
sudo iptables -F
sudo ip6tables -F

# Create the new namespace called napt
ip netns add napt

# Connect the two namespaces through veth pair interfaces
ip link add $inside_global_int type veth peer name $inside_napt_int netns napt

# Send the physical $ce_local_int interface to the new namespace
ip link set $ce_local_int netns napt


# Assign addresses to each interface
ip address add $ce_global_ip dev $ce_global_int
ip address add $inside_global_ip dev $inside_global_int
ip netns exec napt ip address add $inside_napt_ip dev $inside_napt_int
ip netns exec napt ip address add $ce_local_ip dev $ce_local_int

# Activate all interfaces
ip link set $ce_global_int up
ip link set $inside_global_int up
ip netns exec napt ip link set $inside_napt_int up
ip netns exec napt ip link set $ce_local_int up

# Add essential routes to both namespaces
ip netns exec napt ip route add default via $inside_global_ip_no_mask
ip route add 64:ff9b::/96 via $br_global_ip
ip route add $nat44_global_ip/32 via $inside_napt_ip_no_mask

# Turn both namespaces into routers
ip netns exec napt /sbin/sysctl -w net.ipv4.conf.all.forwarding=1
echo 1 > /proc/sys/net/ipv4/ip_forward
echo 1 > /proc/sys/net/ipv6/conf/all/forwarding


# Runing Jool
/sbin/modprobe jool_mapt
jool_mapt instance add "CE 11b" --netfilter --dmr 64:ff9b::/96
jool_mapt -i "CE 11b" global update end-user-ipv6-prefix 2001:db8:ce:11b::/64
jool_mapt -i "CE 11b" global update bmr 2001:db8:ce::/51 $nat44_global_ip_net 13 0
jool_mapt -i "CE 11b" global update map-t-type CE

# NAPT44
sudo /sbin/ip netns exec napt iptables -t nat -A POSTROUTING -s $ce_local_ip_net -o $inside_napt_int -p tcp -j SNAT --to-source $nat44_global_ip:$ports_set
sudo /sbin/ip netns exec napt iptables -t nat -A POSTROUTING -s $ce_local_ip_net -o $inside_napt_int -p udp -j SNAT --to-source $nat44_global_ip:$ports_set
sudo /sbin/ip netns exec napt iptables -t nat -A POSTROUTING -s $ce_local_ip_net -o $inside_napt_int -p icmp -j SNAT --to-source $nat44_global_ip:$ports_set
