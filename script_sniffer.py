import scapy.all as scapy
from datetime import datetime
import sqlite3
######### Joindre à SQL #########
con = sqlite3.connect("sae501.db") #Se connecter au fichier de la bdd sqlite3
cursor = con.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';") # Permet d'afficher les tables pour vérifier la connectivité d'abord
print(cursor.fetchall())
######### Joindre à SQL #########

type_dhcp = ["","Discover","Offer","Request","Decline","ack","nak","release","inform","fore_renew","lease_query","lease_unassigned","lease_unknown","lease_active"]

def packet_handler(packet):
    if packet.haslayer(scapy.IP):
        Src_IP = packet[scapy.IP].src
        Dst_IP = packet[scapy.IP].dst
        Src_MAC = packet[scapy.Ether].src 
        Dst_MAC = packet[scapy.Ether].dst
        Packet_ID = packet[scapy.IP].id
        timestamp = packet.time
        if packet.haslayer(scapy.DHCP):
            dhcp_message_type = packet[scapy.DHCP].options[0][1]
            dhcp_type = type_dhcp[dhcp_message_type]
            date = datetime.fromtimestamp(timestamp, tz = None) 
            print(f"Timestamp: {timestamp}, Date: {date}, Source IP: {Src_IP} -> Destination IP: {Src_IP}, Packet ID: {Packet_ID}, Trame DHCP: {dhcp_type}, Source Mac: {Src_MAC} -> Destination Mac: {Dst_MAC}")
            
			sqlite_insert_query = """INSERT INTO data
                          (Src_IP, Dst_IP, Src_MAC, Dst_MAC, Packet_ID, Time, Heure, Type_Trame) 
                           VALUES 
                          (,,,,)"""

def main(interface):
    scapy.sniff(iface=interface, prn=packet_handler)

if __name__ == "__main__":
    interface = "enp0s31f6"  # Modifier script plus tard pour qu'il prenne l'interface active ou demander interface ?
    main(interface)
