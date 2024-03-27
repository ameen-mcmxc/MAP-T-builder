
## MAP-T Jool Testbed Installation
----
![image](https://user-images.githubusercontent.com/45686881/200935687-7a78400a-2bad-4231-81e7-39e620470644.png)
----

## How to build MAP-T topology 

## Prerequisites:

CE and BR machines have to de Debian 10 (jool software limitation).

The rest of the machines  (IPv4 client, IPv4 server and attacker) can be any Linux distribution that you prefer.

I personally built the whole thing using VMware workstations VMs.

After creating the machines as shown in the above topology. it's time to install everything.

Clone the current repo on all machines.

login as root

## CE machine

`
sudo apt-get update -y
`

`
sudo apt-get install ansible -y
`

`
cd /root/mape-mapt
`

`
ansible-playbook jool
`



MAPe - MAPT IPv6 transition technology.

## MAP-T Topology is shown below: -
