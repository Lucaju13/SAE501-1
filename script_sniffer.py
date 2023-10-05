import scapy.all as scapy

type_dhcp = ["","Discover","Offer","Request","Decline","ack","nak","release","inform","fore_renew","lease_query","lease_unassigned","lease_unknown","lease_active"]

def packet_handler(packet):
    if packet.haslayer(scapy.IP):
        src_ip = packet[scapy.IP].src
        dst_ip = packet[scapy.IP].dst
        src_mac = packet[scapy.Ether].src # Récupère désormais les adresses macs
        dst_mac = packet[scapy.Ether].dst
        packet_id = packet[scapy.IP].id
        timestamp = packet.time
        if packet.haslayer(scapy.DHCP):
            dhcp_message_type = packet[scapy.DHCP].options[0][1]
            dhcp_type = type_dhcp[dhcp_message_type]
            print(f"Timestamp: {timestamp}, Source IP: {src_ip} -> Destination IP: {dst_ip}, Packet ID: {packet_id}, Trame DHCP: {dhcp_type}, Source Mac: {src_mac} -> Destination Mac: {dst_mac}")
            
			# Il faut envoyer ensuite ces informations sur la base de données.

def main(interface):
    scapy.sniff(iface=interface, prn=packet_handler)

if __name__ == "__main__":
    interface = "enp0s31f6"  # Modifier script plus tard pour qu'il prenne l'interface active ou demander interface ?
    main(interface)
