import scapy.all as scapy

# Liste des noms des types de paquet DHCP
type_dhcp = ["","Discover","Offer","Request","Decline","ack","nak","release","inform","fore_renew","lease_query","lease_unassigned","lease_unknown","lease_active"]

def packet_handler(packet):
    if packet.haslayer(scapy.IP):
        src_ip = packet[scapy.IP].src
        dst_ip = packet[scapy.IP].dst
        packet_id = packet[scapy.IP].id
        timestamp = packet.time
        # Suppression du test ICMP pour ne garder que la trame DHCP
        if packet.haslayer(scapy.DHCP):
            dhcp_message_type = packet[scapy.DHCP].options[0][1]
            dhcp_type = type_dhcp[dhcp_message_type]
            print(f"Timestamp: {timestamp}, Source IP: {src_ip} -> Destination IP: {dst_ip}, Packet ID: {packet_id}, Trame DHCP: {dhcp_type}")
            # Affiche désormais toutes les informations lorsque la trame est un DHCP + affiche en même temps le type DHCP
            
			# Il faut envoyer ensuite ces informations sur la base de données.

def main(interface):
    scapy.sniff(iface=interface, prn=packet_handler)

if __name__ == "__main__":
    interface = "enp0s31f6"  # Modifier script plus tard pour qu'il prenne l'interface active ou demander interface ?
    main(interface)
