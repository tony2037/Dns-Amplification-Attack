from scapy.all import *
def pkt_callback(pkt):
    pkt.show()

if __name__ == '__main__':
    sniff(filter = 'udp', prn = pkt_callback)
