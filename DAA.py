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
    parser.add_argument("pos1", help="positional argument 1")
    parser.add_argument("-o", "--optional-arg", help="optional argument", dest="opt", default="default")
    args = parser.parse_args()

    ip = construct_IP()
    udp = construct_UDP()
    dns = construct_DNS()
    q = construct_DNSQR()
    r = Set_UP(ip, udp, dns, q)
    send(r)
