#!/bin/bash

sudo /sbin/ip netns exec napt tc qdisc add dev to_global root handle 1: htb default 1
sudo /sbin/ip netns exec napt tc class add dev to_global parent 1: classid 1:1 htb rate 1gbit
sudo /sbin/ip netns exec napt tc class add dev to_global parent 1:1 classid 1:10 htb rate 10kbit ceil 10kbit
sudo /sbin/ip netns exec napt tc qdisc add dev to_global parent 1:10 handle 10: sfq perturb 10
sudo /sbin/ip netns exec napt tc filter add dev to_global parent 1:0 protocol ip prio 1 u32 match ip protocol 17 0xff match ip dport 53 0xffff flowid 1:10
sudo /sbin/ip netns exec napt tc filter add dev to_global parent 1:0 protocol ip prio 2 u32 match ip protocol 17 0xff match ip dport 53 0xffff match u32 0 0 flowid 1:10 action drop



# To delete the effect of tc commands, apply the below command
#sudo /sbin/ip netns exec napt tc qdisc del dev to_global root
