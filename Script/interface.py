import tkinter as tk
from tkinter import ttk
import requests
import json
from script_sniffer import main as sniff_packets
import threading

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Projet Logiciel")
        self.geometry("1500x630")
        self.create_widgets()
        self.setup_api()
        self.configure(bg="#B0E0E6")

    def afficher_message(self, message):
        """Fonction pour afficher un message dans la boîte de texte du dashboard."""
        self.box_affichage_tests.config(state="normal")
        self.box_affichage_tests.insert(tk.END, message + "\n")
        self.box_affichage_tests.config(state="disabled")

    def start_sniffing(self):
        self.afficher_message("Scan des paquets lancé.")
        self.sniffing_active = True
        interface = "enp0s3"
        sniff_packets(interface, self)

    def start_sniffing_threaded(self):
        self.sniffing_thread = threading.Thread(target=self.start_sniffing)
        self.sniffing_thread.start()

    def stop_sniffing(self):
        self.afficher_message("Scan des paquets arrêté.")
        self.sniffing_active = False

    def create_widgets(self):
        # Box d'affichage (Dashboard)
        test_unitaires = tk.Label(self, text="Dashboard")
        test_unitaires.pack(anchor="w")
        self.box_affichage_tests = tk.Text(self, bg="#D3D3D3",height=10, width=50)
        self.box_affichage_tests.pack(anchor="w")

        # Box d'affichage des erreurs
        erreurs = tk.Label(self,text="Detection d'alertes")
        erreurs.place(x=950, y=1)
        self.box_affichage_erreurs = tk.Text(self,bg="#D3D3D3", height=10, width=123)
        self.box_affichage_erreurs.place(x=500, y=20)

        # Ajout des combobox
        filtre_label = ttk.Label(self, text="Filtres :")
        filtre_label.place(x=500, y=350)

        # Création de la combobox pour le filtre 1
        self.filtre_2_var = tk.StringVar()
        self.filtre_2_combobox = ttk.Combobox(self, textvariable=self.filtre_2_var, values=["Request", "nak", "Offer", "ack"])
        self.filtre_2_combobox.place(x=600, y=350)
        self.filtre_2_combobox.bind("<<ComboboxSelected>>", lambda event: self.afficher_filtre())

        # Boutons
        btn_sortir = ttk.Button(self, text="Sortir du programme", command=self.quit)
        btn_sortir.place(x=1200, y=250)

        # Ajout du bouton pour afficher les statistiques
        btn_afficher_statistiques = ttk.Button(self, text="Stats", command=self.afficher_statistiques)
        btn_afficher_statistiques.place(x=20, y=250)

        # Bouton lancer scan DHCP
        btn_scan_packets = ttk.Button(self, text="Scan des paquets", command=self.start_sniffing_threaded)
        btn_scan_packets.place(x=20, y=290)

        # Bouton stop scan DHCP
        btn_stop_sniffing = ttk.Button(self, text="Arrêter le sniffing", command=self.stop_sniffing)
        btn_stop_sniffing.place(x=250, y=290)

        # Création du tableau
        columns = ('ID', 'IP SRC', 'IP DST', 'MAC SRC', 'MAC DST', 'PACKET ID', 'TIMESTAMP', 'DATE', 'TYPE')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')

        self.tree.tag_configure("background_column", background="#D3D3D3")

        self.tree.place(x=20, y=380) 

        for col in columns:
            self.tree.heading(col, text=col, command=lambda c=col: self.trier_colonne(c))  # Lier la fonction de triage
            self.tree.column(col, width=163)
        self.tree.place(x=20, y=380)

        # Bouton pour afficher les données dans la table
        btn_afficher_donnees = ttk.Button(self, text="Afficher les données", command=self.afficher_filtre)
        btn_afficher_donnees.place(x=20, y=340)

        # Bouton pour détecter les alertes
        btn_detecter_alertes = ttk.Button(self, text="Lancer la détection d'alertes", command=self.detecter_alertes)
        btn_detecter_alertes.place(x=600, y=250)

    #------------------------------------Fonctions-------------------------------
    def setup_api(self):
        self.response_API = requests.get('http://localhost:5000/api/elements')
        if self.response_API.status_code == 200:
            self.data = self.response_API.text
            self.box_affichage_tests.insert(tk.END, "Connexion API REST bien établie.\n")  # Ajout de ce message dans le dashboard
        else:
            self.box_affichage_tests.insert(tk.END, f"Connexion échouée, status code: {self.response_API.status_code}\n")  # Ajout de ce message dans le dashboard
        self.box_affichage_tests.config(state="disabled")

    def detecter_alertes(self):
        self.box_affichage_erreurs.delete(1.0, tk.END)  # Efface le contenu actuel

        self.parse_json = json.loads(self.data)

        for trame in self.parse_json:
            ip_dst = trame.get('Dst_IP', '') 
            if not (ip_dst.startswith('10.202.') or ip_dst.startswith('10.203.') or ip_dst.startswith('255.255.255.255')):
                message = f"Alerte détectée: Adresse IP hors du sous-réseau autorisé. Trame: {trame}"
                self.box_affichage_erreurs.insert(tk.END, message + "\n")
                self.box_affichage_erreurs.tag_configure("rouge", foreground="red")
                self.box_affichage_erreurs.tag_add("rouge", "1.0", "end",)
                self.box_affichage_erreurs.config(state="disabled")

    def afficher_filtre(self):
        selected_filtre = self.filtre_2_var.get()
        self.parse_json = json.loads(self.data)

        for row in self.tree.get_children():
            self.tree.delete(row)

        if selected_filtre:
            filtered_data = [trame for trame in self.parse_json if trame.get('Type_Trame', '') == selected_filtre]
        else:
            filtered_data = self.parse_json

        for row in filtered_data:
            values = (
                row.get('ID', ''),
                row.get('Src_IP', ''),
                row.get('Dst_IP', ''),
                row.get('Src_MAC', ''),
                row.get('Dst_MAC', ''),
                row.get('Packet_ID', ''),
                row.get('Time', ''),
                row.get('Heure', ''),
                row.get('Type_Trame', '')
            )
            self.tree.insert('', 'end', values=values)

    def afficher_statistiques(self):
        self.box_affichage_tests.config(state="normal")
        self.box_affichage_tests.delete(1.0, tk.END)

        self.parse_json = json.loads(self.data)

        # dictionnaire pour stocker le nombre de trames par type
        type_count = {}

        for trame in self.parse_json:
            type_trame = trame.get('Type_Trame', '')
            
            # Si le type de trame n'est pas déjà dans le dictionnaire, ajoutez-le
            if type_trame not in type_count:
                type_count[type_trame] = 1
            else:
                type_count[type_trame] += 1

        total_requetes = sum(type_count.values())

        for type_trame, count in type_count.items():
            self.box_affichage_tests.insert(tk.END, f"{type_trame}: {count} requetes\n")

        # Ligne pour afficher le nombre total de trames
        self.box_affichage_tests.insert(tk.END, f"\nNombre total de trames: {total_requetes}\n")

        self.box_affichage_tests.config(state="disabled")


    def trier_colonne(self, colonne):
        """Fonction pour trier le tableau en fonction de la colonne cliquée."""
        # Récupère tous les éléments actuellement dans le tableau
        data = [(self.tree.set(child, colonne), child) for child in self.tree.get_children("")]

        # Trie le Treeview en fonction de la colonne
        data.sort()

        # Trie le Treeview en fonction de la colonne
        for i, item in enumerate(data):
            self.tree.move(item[1], "", i)
                 
if __name__ == "__main__":
    app = App()
    app.mainloop()
