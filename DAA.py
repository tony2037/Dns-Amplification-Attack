from scapy.all import *

# Construct IP packet
ip = IP()
ip.show()

# Construct UDP packet
udp = UDP()
u.display()

# Construct DNS packet
dns = DNS()
dns.display()

# Construct DNS Question Record
q = DNSQR()
q.display()

# Set DNS Question Record in DNS packet
dns.qd = q

# Concencate
r = (ip/udp/dns)
r.display()
sr1(r)

# Set up r
r.src = ''
r = (ip/udp/dns)
r.display()
send(r)

