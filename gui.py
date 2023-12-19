import tkinter as tk
from tkinter import ttk 
import sqlite3

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Projet Logiciel")
        self.geometry("1500x630")

        self.create_widgets()
        self.setup_database()

    def create_widgets(self):

        # Box d'affichage des résultats de Test Unitaires
        test_unitaires = tk.Label(self, text="Résultat tests unitaires")
        test_unitaires.pack(anchor="w")
        self.box_affichage_tests = tk.Text(self, height=10, width=50)
        self.box_affichage_tests.pack(anchor="w")

        # Box d'affichage des erreurs
        erreurs = tk.Label(self, text="Detection d'alertes")
        erreurs.place(x=950, y=1)
        self.box_affichage_erreurs = tk.Text(self, height=10, width=123)
        self.box_affichage_erreurs.place(x=500, y=20)

        # Ajout des combobox
        filtre_label = ttk.Label(self, text="Filtres :")
        filtre_label.place(x=500, y=350)

        # Création de la combobox pour le filtre 1
        self.filtre_2_var = tk.StringVar()
        self.filtre_2_combobox = ttk.Combobox(self, textvariable=self.filtre_2_var, values=["Request","nak","Offer","ack"])
        self.filtre_2_combobox.place(x=600, y=350)

        # Boutons
        btn_sortir = tk.Button(self, text="Sortir du programme", command=self.quit)
        btn_sortir.place(x=1200, y=250) 

        # Ajout du bouton pour afficher les statistiques
        btn_afficher_statistiques = tk.Button(self, text="Statistiques", command=self.afficher_statistiques)
        btn_afficher_statistiques.place(x=20, y=250)


        # Création du tableau
        columns = ('ID', 'IP SRC', 'IP DST', 'MAC SRC', 'MAC DST', 'PACKET ID', 'TIMESTAMP', 'DATE', 'TYPE')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')

        for col in columns:
            self.tree.heading(col, text=col, command=lambda c=col: self.trier_colonne(c))
            self.tree.column(col, width=163)

        self.tree.place(x=20, y=380)  

        # Bouton pour afficher les données dans la table
        btn_afficher_donnees = tk.Button(self, text="Afficher les données", command=self.afficher_filtre)
        btn_afficher_donnees.place(x=20, y=340)

        # Bouton pour détecter les alertes
        btn_detecter_alertes = tk.Button(self, text="Lancer la détection d'alertes", command=self.detecter_alertes)
        btn_detecter_alertes.place(x=600, y=250)
#------------------------------------Fonctions-------------------------------
    def setup_database(self):
        self.conn = sqlite3.connect('sae501.db')
        self.cursor = self.conn.cursor()

    def detecter_alertes(self):
        self.box_affichage_erreurs.delete(1.0, tk.END)  # Efface le contenu actuel

        self.cursor.execute("SELECT * FROM data")
        trames = self.cursor.fetchall()

        for trame in trames:
            ip_dst = trame[2]
            if not (ip_dst.startswith('10.202.') or ip_dst.startswith('10.203.') or ip_dst.startswith('255.255.255.255')):
                message = f"Alerte détectée: Adresse IP hors du sous-réseau autorisé. Trame: {trame}"
                self.box_affichage_erreurs.insert(tk.END, message + "\n")
                self.box_affichage_erreurs.tag_configure("rouge", foreground="red")
                self.box_affichage_erreurs.tag_add("rouge", "1.0", "end",)
                self.box_affichage_erreurs.config(state="disabled")
                
    
    def afficher_statistiques(self):
        self.cursor.execute("SELECT Type_Trame, COUNT(*) FROM data GROUP BY Type_Trame")
        statistiques = self.cursor.fetchall()

        # Afficher les statistiques dans la boîte de texte des statistiques
        self.box_affichage_tests.config(state="normal")
        self.box_affichage_tests.delete(1.0, tk.END)

        total_requetes = 0  # Nouvelle variable pour stocker le nombre total de requêtes

        for stat in statistiques:
            self.box_affichage_tests.insert(tk.END, f"{stat[0]}: {stat[1]} requêtes\n")
            total_requetes += stat[1]  # Ajoute le nombre de requêtes de chaque type au total

        # La ligne pour afficher le nombre total de requêtes
        self.box_affichage_tests.insert(tk.END, f"\nNombre total de requêtes: {total_requetes}\n")

        self.box_affichage_tests.config(state="disabled")
    
    def afficher_filtre(self):
        selected_filtre = self.filtre_2_var.get()

        for row in self.tree.get_children():
            self.tree.delete(row)

        if selected_filtre:
            self.cursor.execute(f"SELECT * FROM data WHERE Type_Trame = '{selected_filtre}'")
        else:
            self.cursor.execute("SELECT * FROM data")

        for row in self.cursor.fetchall():
            self.tree.insert('', 'end', values=row)

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
