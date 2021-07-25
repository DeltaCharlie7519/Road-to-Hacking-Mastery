import scapy.all as scapy


def scan_ip_add(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #default destination Mac for broadcast MAC derived from the ether frame
    arp_request_broadcast = arp_request/broadcast #appends packets
    answered, unanswered = scapy.srp(arp_request_broadcast,timeout = 1) #.srp returns lists in form of response from the broadcast
    print(answered.summary())
#.show() shows the details of each packets in columns unlike a statement in .summary()

scan_ip_add("10.0.2.0/24")
