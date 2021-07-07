import scapy.all as scapy


def scan_ip_add(ip):
    arp_request = scapy.ARP(pdst=ip)
    arp_request.pdst = ip
    print(arp_request.summary())
    scapy.ls(scapy.ARP)


scan_ip_add("10.0.2.1/24")
