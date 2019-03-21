from scapy.all import *

from argparse import ArgumentParser
import sys

def construct_IP():
    # Construct IP packet
    ip = IP()
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
    dns.display()
    return dns

def construct_DNSQR():
    # Construct DNS Question Record
    q = DNSQR()
    q.display()
    return q

def Set_UP(ip, udp, dns, q):
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
    return r

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-D", "--optional-arg", help="Assign specific DNS server", dest="dserver", default="default")
    parser.add_argument("-T", "--optional-arg", help="target server", dest="target", default="default")
    args = parser.parse_args()
    print('DNS server: %s' %args.dserver)
    print('Target: %s' %args.target)

    ip = construct_IP()
    udp = construct_UDP()
    dns = construct_DNS()
    q = construct_DNSQR()
    r = Set_UP(ip, udp, dns, q)
    send(r)
