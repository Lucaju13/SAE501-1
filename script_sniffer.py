import scapy.all as scapy

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
        elif packet.haslayer(scapy.DHCP): #Remarque si il a une trame DHCP
            dhcp_message_type = packet[scapy.DHCP].options[0][1]
            if dhcp_message_type == 2:
                dhcp_type = "DHCP Offer"
            elif dhcp_message_type == 5:
                dhcp_type = "DHCP ACK"
            else:
                dhcp_type = f"DHCP Type {dhcp_message_type}"
            print(dhcp_type)

def main(interface):
    scapy.sniff(iface=interface, prn=packet_handler)

if __name__ == "__main__":
    interface = "enp0s31f6" 
    main(interface)
