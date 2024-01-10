import scapy.all as scapy
from datetime import datetime
import sqlite3

type_dhcp = ["","Discover","Offer","Request","Decline","ack","nak","release","inform","force_renew","lease_query","lease_unassigned","lease_unknown","lease_active"]

sniffing_active = True  # Variable qui sert à renseigner si le sniffing doit être actif ou pas

def stop_sniffing():
	global sniffing_active
	sniffing_active = False

def packet_handler(packet):
	print("test") # Print qui me permet de voir si le script tourne puis si il est arrêté
	con = sqlite3.connect("sae501.db") #
	cursor = con.cursor() #
	global sniffing_active
	if not sniffing_active:
		return

	if packet.haslayer(scapy.IP):
		Src_IP = packet[scapy.IP].src
		Dst_IP = packet[scapy.IP].dst
		Src_MAC = packet[scapy.Ether].src 
		Dst_MAC = packet[scapy.Ether].dst
		Packet_ID = packet[scapy.IP].id
		timestamp = packet.time
		
		if packet.haslayer(scapy.DHCP) and packet[scapy.DHCP].options[0][1] != 1:
			dhcp_message_type = packet[scapy.DHCP].options[0][1]
			dhcp_type = type_dhcp[dhcp_message_type]
			date = datetime.fromtimestamp(timestamp, tz = None) 
			print(f"Timestamp: {timestamp}, Date: {date}, Source IP: {Src_IP} -> Destination IP: {Dst_IP}, Packet ID: {Packet_ID}, Trame DHCP: {dhcp_type}, Source Mac: {Src_MAC} -> Destination Mac: {Dst_MAC}") 
			sqlite_insert_query = """INSERT INTO data
						  (Src_IP, Dst_IP, Src_MAC, Dst_MAC, Packet_ID, Time, Heure, Type_Trame) 
						   VALUES 
						  (?,?,?,?,?,?,?,?)"""
			data_tuple = (Src_IP, Dst_IP, Src_MAC, Dst_MAC, Packet_ID, timestamp, date, dhcp_type) 
			cursor.execute(sqlite_insert_query, data_tuple) 
			con.commit()
			cursor.close() #
			con.close() #
			
def main(interface):
	scapy.sniff(iface=interface, prn=packet_handler)
	
if __name__ == "__main__":
	interface = "eno1"  # On n'a plus besoin de modifier l'adresse si on fait sur un raspberry
	main(interface)
    
#Notes: Faire en sorte que le script tourne selon une fonction en renseignant une durée de script.
#Et transformer le script gui pour tester un bouton pour lancer le script sur une 1ère durée
