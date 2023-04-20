

## Explaining "traffic-controller.sh" script

Those command creates a hierarchical token bucket (HTB) qdisc on the to\_global interface with a default class (1:1)

and a child class(1:10) for DNS traffic.

The child class is limited to 10 kilobits per second (htb rate 10kbit) and is configured with 

a stochastic fair queue (SFQ) qdisc (tc qdisc add dev to\_global parent 1:10 handle 10: sfq perturb 10)

to spread out the limited bandwidth across multiple flows.

``

The tc filter command then applies two filters to the ingress traffic on the to\_global interface.

The first filter matches incoming DNS queries (match ip protocol 17 0xff match ip dport 53 0xffff) 

and sends them to the child class (flowid 1:10). The second filter matches any traffic that exceeds 

the rate limit (match u32 0 0) and drops it (action drop).


