## Modules ##
import scapy.all as scapy
from datetime import datetime
import sqlite3

## Variables ##
type_dhcp = ["","Discover","Offer","Request","Decline","ack","nak","release","inform","force_renew","lease_query","lease_unassigned","lease_unknown","lease_active"] # Liste des types de paquets DHCP
sniffing_active = True  # Variable qui sert à renseigner si le sniffing doit être actif ou pas

## Fonctions ##
def packet_handler(packet, app_instance):
	if not app_instance.sniffing_active: # Le script ne s'exécute pas si le flag est désactivé, donc si le bouton stop est cliqué
		return
	con = sqlite3.connect("sae501.db") # Connexion à la base de données
	cursor = con.cursor()

	if packet.haslayer(scapy.IP): # On récupère les informations IP, MAC et timestamp du paquet si il y a une couche IP
		Src_IP = packet[scapy.IP].src
		Dst_IP = packet[scapy.IP].dst
		Src_MAC = packet[scapy.Ether].src 
		Dst_MAC = packet[scapy.Ether].dst
		Packet_ID = packet[scapy.IP].id
		timestamp = packet.time
		
		if packet.haslayer(scapy.DHCP) and packet[scapy.DHCP].options[0][1] != 1: # On récupère l'heure, le type de message et le type de trame DHCP si c'est une trame DHCP
			dhcp_message_type = packet[scapy.DHCP].options[0][1]
			dhcp_type = type_dhcp[dhcp_message_type]
			date = datetime.fromtimestamp(timestamp, tz = None) 
			# Envoie dans la console des informations récupérées
			print(f"Timestamp: {timestamp}, Date: {date}, Source IP: {Src_IP} -> Destination IP: {Dst_IP}, Packet ID: {Packet_ID}, Trame DHCP: {dhcp_type}, Source Mac: {Src_MAC} -> Destination Mac: {Dst_MAC}") 
			# Création d'une insert query SQLite avec les différentes variables de la table data, les valeurs étant d'abord renseignées par des "?"
			sqlite_insert_query = """INSERT INTO data 
						  (Src_IP, Dst_IP, Src_MAC, Dst_MAC, Packet_ID, Time, Heure, Type_Trame) 
						   VALUES 
						  (?,?,?,?,?,?,?,?)"""
			# Création d'un tuple avec les différentes valeurs récupérés, dans le même ordre auquel les variables de la table ont été renseignés.
			data_tuple = (Src_IP, Dst_IP, Src_MAC, Dst_MAC, Packet_ID, timestamp, date, dhcp_type) 
			# L'envoie des données avec la requête SQLite et les valeurs renseignées dans le tuple est exécuté.
			cursor.execute(sqlite_insert_query, data_tuple) 
			# L'envoie est confirmée.
			con.commit()
			# La connexion à la base de données se ferme.
			cursor.close()
			con.close()
			
def main(interface, app_instance):
    while app_instance.sniffing_active: # Flag pour que le script continue tant que le bouton n'est pas cliqué
        scapy.sniff(iface=interface, prn=lambda pkt: packet_handler(pkt, app_instance))

## Bloc Principal ##
if __name__ == "__main__":
	interface = "eno1"  # Interfaces rasp: eth0 et wlan0
	main(interface)
