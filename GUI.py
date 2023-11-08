import tkinter as tk
from tkinter import ttk 
import sqlite3

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Projet Logiciel")
        self.geometry("950x630")

        self.create_widgets()
        self.setup_database()

    def create_widgets(self):
        # Box pour prendre l’adresse API REST
        api = tk.Label(self, text= "API REST URL")
        api.pack()
        self.box_adresse_api = tk.Entry(self, width=50)
        self.box_adresse_api.pack()

        # Box d'affichage des résultats de Test Unitaires
        test_unitaires = tk.Label(self, text="Résultat tests unitaires")
        test_unitaires.pack(anchor="w")
        self.box_affichage_tests = tk.Text(self, height=10, width=50)
        self.box_affichage_tests.pack(anchor="w")

        # Box d'affichage des erreurs
        erreurs = tk.Label(self, text="Detection d'alertes")
        erreurs.place(x=650, y=45)
        self.box_affichage_erreurs = tk.Text(self, height=10, width=50)
        self.box_affichage_erreurs.place(x=500, y=65)

        # Ajout des combobox
        filtre_label = ttk.Label(self, text="Filtres :")
        filtre_label.place(x=500, y=330)

        # Création de la combobox pour le filtre 1
        self.filtre_1_var = tk.StringVar()
        self.filtre_1_combobox = ttk.Combobox(self, textvariable=self.filtre_1_var, values=["Date", "Type de requete", "Type d'erreur"])
        self.filtre_1_combobox.place(x=500, y=350)

        # Création de la combobox pour le filtre 2
        self.filtre_2_var = tk.StringVar()
        self.filtre_2_combobox = ttk.Combobox(self, textvariable=self.filtre_2_var, values=["Date", "Type de requete", "Type d'erreur"])
        self.filtre_2_combobox.place(x=600, y=350)

        # Boutons
        btn_lancer_requete = tk.Button(self, text="Lancer la requête", command=self.lancer_requete)
        btn_lancer_requete.place(x=20, y=250)

        btn_sortir = tk.Button(self, text="Sortir du programme", command=self.quit)
        btn_sortir.place(x=750, y=250) 

        # Création du tableau
        columns = ('ID', 'IP SRC', 'IP DST', 'MAC SRC', 'MAC DST', 'PACKET ID','TIMESTAMP','DATE', 'TYPE')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.tree.place(x=20, y=380) 

        # Bouton pour afficher les données dans la table
        btn_afficher_donnees = tk.Button(self, text="Afficher les données", command=self.afficher_donnees)
        btn_afficher_donnees.place(x=20, y=340)

        # Bouton pour détecter les alertes
        btn_detecter_alertes = tk.Button(self, text="Lancer la détection d'alertes", command=self.detecter_alertes)
        btn_detecter_alertes.place(x=300, y=250)

    def setup_database(self):
        self.conn = sqlite3.connect('sae501.db')
        self.cursor = self.conn.cursor()

    def afficher_donnees(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        self.cursor.execute("SELECT * FROM data")
        for row in self.cursor.fetchall():
            self.tree.insert('', 'end', values=row)

    def lancer_requete(self):
        # Ajoutez ici le code pour lancer la requête
        pass


    def detecter_alertes(self):
        self.box_affichage_erreurs.delete(1.0, tk.END)  # Efface le contenu actuel

        self.cursor.execute("SELECT * FROM data")
        trames = self.cursor.fetchall()

        for trame in trames:
            ip_dst = trame[2]
            if not (ip_dst.startswith('10.202.') or ip_dst.startswith('10.203.')):
                message = f"Alerte détectée: Adresse IP hors du sous-réseau autorisé. Trame: {trame}"
                self.box_affichage_erreurs.insert(tk.END, message + "\n")
                self.box_affichage_erreurs.tag_configure("rouge", foreground="red")
                self.box_affichage_erreurs.tag_add("rouge", "1.0", "end")

if __name__ == "__main__":
    app = App()
    app.mainloop()
