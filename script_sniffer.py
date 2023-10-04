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

def main(interface):
    scapy.sniff(iface=interface, prn=packet_handler)

if __name__ == "__main__":
    interface = "enp0s31f6" 
    main(interface)
