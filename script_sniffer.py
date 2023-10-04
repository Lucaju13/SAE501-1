import scapy.all as scapy

#Liste des noms des types de paquet DHCP
type_dhcp = ["","Discover","Offer","Request","Decline","ack","nak","release","inform","fore_renew","lease_query","lease_unassigned","lease_unknown","lease_active"]

def packet_handler(packet):
    if packet.haslayer(scapy.IP):
        src_ip = packet[scapy.IP].src
        dst_ip = packet[scapy.IP].dst
        packet_id = packet[scapy.IP].id
        timestamp = packet.time
        print(f"Timestamp: {timestamp}, Source IP: {src_ip} -> Destination IP: {dst_ip}, Packet ID: {packet_id}")
        if packet.haslayer(scapy.ICMP):
           icmp_type = packet[scapy.ICMP].type
           if icmp_type == 0:
               print("Réussite")
           else:
               print("Échec")
        elif packet.haslayer(scapy.DHCP):
            dhcp_message_type = packet[scapy.DHCP].options[0][1]
            dhcp_type = type_dhcp[dhcp_message_type] #Récupère le nom du paquet dhcp selon le type
            print(dhcp_type)

def main(interface):
    scapy.sniff(iface=interface, prn=packet_handler)

if __name__ == "__main__":
    interface = "enp0s31f6"  # Remplacez par le nom de votre interface réseau
    main(interface)
