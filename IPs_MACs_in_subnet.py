import scapy.all as scapy


def scan_ip_add(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # default destination Mac for broadcast MAC derived from the ether frame
    arp_request_broadcast = arp_request/broadcast  # appends packets
    answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=True)[0]  # .srp returns 2 lists in form of response from the broadcast
    clients_list = []
    for element in answered:
        client_dictionary = {"ip": element[1].psrc, "MAC": element[1].hwsrc}
        clients_list.append(client_dictionary)

    return clients_list    # returning IP Addresses,MAC Addresses from the clients
# .show() shows the details of each packets in columns unlike a statement in .summary()


def print_result(result):
    print("IP\t\t\tMAC")
    for client in result:
        print(client["ip"]+"\t\t"+client["MAC"])


scan_result = scan_ip_add("10.0.2.1/24")
print_result(scan_result)
