import scapy.all as scapy


def scan_ip_add(ip):
    arp_request = scapy.ARP(pdst=ip)
    arp_request.show()
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast.show()
    arp_request_broadcast = arp_request/broadcast
    arp_request_broadcast.show()


scan_ip_add("10.0.2.1/24")
