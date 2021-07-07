import scapy.all as scapy


def scan_ip_add(ip):
    scapy.arping(ip)


scan_ip_add("10.0.2.1/24")
