import tkinter as tk
from tkinter import ttk
import datetime
import requests
import json
from script_sniffer import main as sniff_packets
import threading

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Projet Logiciel")
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
        test_unitaires.grid(row=0, column=0, sticky="w")
        self.box_affichage_tests = tk.Text(self, bg="#D3D3D3", height=10, width=50)
        self.box_affichage_tests.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)  # Utilisation de sticky pour étirer dans toutes les directions
        self.box_affichage_tests.grid_columnconfigure(0, weight=1)  # Permet à la colonne de s'étirer

        # Box d'affichage des erreurs
        erreurs = tk.Label(self, text="Detection d'alertes")
        erreurs.grid(row=0, column=1, padx=10, pady=10)
        self.box_affichage_erreurs = tk.Text(self, bg="#D3D3D3", height=10, width=123)
        self.box_affichage_erreurs.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
        self.box_affichage_erreurs.grid_columnconfigure(0, weight=1)  # Permet à la colonne de s'étirer

        # Ajout des combobox
        filtre_label = ttk.Label(self, text="Filtres:")
        filtre_label.grid(row=5, column=0, padx=10, pady=1, sticky="w")

        # Création de la combobox pour le filtre 1
        self.filtre_2_var = tk.StringVar()
        self.filtre_2_combobox = ttk.Combobox(self, textvariable=self.filtre_2_var, values=["Request", "nak", "Offer", "ack"])
        self.filtre_2_combobox.grid(row=5, column=0, padx=100, pady=10, sticky="w")
        self.filtre_2_combobox.bind("<<ComboboxSelected>>", lambda event: self.afficher_filtre())

        # Création de la combobox pour le filtre de période
        periode_label = ttk.Label(self, text="Période :")
        periode_label.grid(row=5, column=1, padx=5, pady=10, sticky="w")

        self.periode_var = tk.StringVar()
        self.periode_combobox = ttk.Combobox(self, textvariable=self.periode_var,
                                            values=["10 minutes", "30 minutes", "1 heure", "5 heures",
                                                    "12 heures", "24 heures", "1 semaine", "1 mois"])
        self.periode_combobox.grid(row=5, column=1, padx=100, pady=10, sticky="w")
        self.periode_combobox.bind("<<ComboboxSelected>>", lambda event: self.afficher_filtre())



        # Boutons
        btn_sortir = ttk.Button(self, text="Sortir du programme", command=self.quit)
        btn_sortir.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        btn_afficher_statistiques = ttk.Button(self, text="Stats", command=self.afficher_statistiques)
        btn_afficher_statistiques.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        btn_scan_packets = ttk.Button(self, text="Scan des paquets", command=self.start_sniffing_threaded)
        btn_scan_packets.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        btn_stop_sniffing = ttk.Button(self, text="Arrêter le sniffing", command=self.stop_sniffing)
        btn_stop_sniffing.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

        btn_afficher_donnees = ttk.Button(self, text="Afficher les données", command=self.afficher_filtre)
        btn_afficher_donnees.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

        btn_detecter_alertes = ttk.Button(self, text="Lancer la détection d'alertes", command=self.detecter_alertes)
        btn_detecter_alertes.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

        # Création du tableau
        columns = ('ID', 'IP SRC', 'IP DST', 'MAC SRC', 'MAC DST', 'PACKET ID', 'TIMESTAMP', 'DATE', 'TYPE')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        self.tree.tag_configure("background_column", background="#D3D3D3")

        for col in columns:
            self.tree.heading(col, text=col, command=lambda c=col: self.trier_colonne(c))
            self.tree.column(col, width=163)
        self.tree.grid(row=8, column=0, columnspan=3, pady=10, sticky="nsew")

        # Création des barres de défilement
        scrollbar_y = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        scrollbar_y.grid(row=8, column=3, sticky="ns")

        scrollbar_x = ttk.Scrollbar(self, orient="horizontal", command=self.tree.xview)
        scrollbar_x.grid(row=9, column=0, columnspan=3, sticky="ew")

        # Lier les barres de défilement au Treeview
        self.tree.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

        self.grid_rowconfigure(1, weight=1)  # La ligne de l'affichage du tableau peut être étirée
        self.grid_columnconfigure(0, weight=1)  # La colonne de l'affichage du tableau peut être étirée

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
                self.box_affichage_erreurs.config(state="normal")
                self.box_affichage_erreurs.insert(tk.END, message + "\n", "rouge")  # Balisez le message avec "rouge"
                self.box_affichage_erreurs.config(state="disabled")

                # indication visuelle dans le tableau
                self.ajouter_ligne_tableau(trame, rouge=True)
            else:
                # ligne normale dans le tableau
                self.ajouter_ligne_tableau(trame, rouge=False)

        # Configuration de l'étiquette pour la couleur rouge
        self.box_affichage_erreurs.tag_configure("rouge", foreground="red")

    def ajouter_ligne_tableau(self, trame, rouge=False):
        values = (
            trame.get('ID', ''),
            trame.get('Src_IP', ''),
            trame.get('Dst_IP', ''),
            trame.get('Src_MAC', ''),
            trame.get('Dst_MAC', ''),
            trame.get('Packet_ID', ''),
            trame.get('Time', ''),
            trame.get('Heure', ''),
            trame.get('Type_Trame', '')
        )
        # Configuration de couleur différente pour les lignes d'alerte dans le tableau
        tags = () if not rouge else ("rouge_tableau",)
        self.tree.insert('', 'end', values=values, tags=tags)

        # Configuration de l'étiquette pour la couleur rouge dans le tableau
        self.tree.tag_configure("rouge_tableau", background="red", foreground="white")

    def afficher_filtre(self):
        selected_filtre = self.filtre_2_var.get()
        selected_periode = self.periode_var.get()
        self.parse_json = json.loads(self.data)

        for row in self.tree.get_children():
            self.tree.delete(row)

        if selected_filtre:
            filtered_data = [trame for trame in self.parse_json if trame.get('Type_Trame', '') == selected_filtre]
        else:
            filtered_data = self.parse_json

        if selected_periode:
            now = datetime.datetime.now()
            if selected_periode == "10 minutes":
                filtered_data = [trame for trame in filtered_data if self.est_dans_periode(trame, now, 10)]
            elif selected_periode == "30 minutes":
                filtered_data = [trame for trame in filtered_data if self.est_dans_periode(trame, now, 30)]
            elif selected_periode == "1 heure":
                filtered_data = [trame for trame in filtered_data if self.est_dans_periode(trame, now, 60)]
            elif selected_periode == "5 heures":
                filtered_data = [trame for trame in filtered_data if self.est_dans_periode(trame, now, 300)]
            elif selected_periode == "12 heures":
                filtered_data = [trame for trame in filtered_data if self.est_dans_periode(trame, now, 720)]
            elif selected_periode == "24 heures":
                filtered_data = [trame for trame in filtered_data if self.est_dans_periode(trame, now, 1440)]
            elif selected_periode == "1 semaine":
                filtered_data = [trame for trame in filtered_data if self.est_dans_periode(trame, now, 10080)]
            elif selected_periode == "1 mois":
                filtered_data = [trame for trame in filtered_data if self.est_dans_periode(trame, now, 43200)]

        for trame in filtered_data:
            self.ajouter_ligne_tableau(trame, rouge=False)

    def est_dans_periode(self, trame, now, minutes):
        timestamp = datetime.datetime.strptime(trame.get('Time', ''), "%Y-%m-%d %H:%M:%S")
        diff = now - timestamp
        return diff.total_seconds() / 60 <= minutes
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
    app.geometry("800x600")  # Dimensions initiales
    app.minsize(500, 400)    # Dimensions minimales
    app.grid_rowconfigure(1, weight=1)  # Permet à la ligne principale de s'étirer
    app.grid_columnconfigure(0, weight=1)  # Permet à la colonne principale de s'étirer
    app.mainloop()
