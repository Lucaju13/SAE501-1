import tkinter as tk
from tkinter import ttk 
import sqlite3
def lancer_requete():
    # Ajoutez ici le code pour lancer la requête
    pass

def sauvegarder():
    # Ajoutez ici le code pour sauvegarder dans la base de données
    pass


# Création de la fenêtre principale
root = tk.Tk()
root.title("Projet Logiciel")

largeur = 950
hauteur = 630
resolution = f"{largeur}x{hauteur}"
root.geometry(resolution)

# Box pour prendre l’adresse API REST
api = tk.Label(root, text= "API REST URL")
api.pack()
box_adresse_api = tk.Entry(root, width=50)
box_adresse_api.pack()

# Box d'affichage des résultats de Test Unitaires
test_unitaires = tk.Label(root, text="Résultat tests unitaires")
test_unitaires.pack(anchor="w")
box_affichage_tests = tk.Text(root, height=10, width=50)
box_affichage_tests.pack(anchor="w")

# Box d'affichage des erreurs
erreurs = tk.Label(root, text="Detenction d'alertes")
erreurs.place(x=650, y=45)
box_affichage_erreurs = tk.Text(root, height=10, width=50)
box_affichage_erreurs.place(x=500, y=65)

# Boutons
btn_lancer_requete = tk.Button(root, text="Lancer la requête", command=lancer_requete)
btn_lancer_requete.place(x=20, y=250)

btn_stop = tk.Button(root, text="Stop", command=root.quit)  # Ajoutez la fonction associée
btn_stop.place(x=600, y=250) 

btn_sortir = tk.Button(root, text="Sortir du programme", command=root.quit)
btn_sortir.place(x=750, y=250)


btn_sauvegarder = tk.Button(root, text="Sauvegarder", command=sauvegarder)
btn_sauvegarder.place(x=300, y=250) 


# Ajout des combobox
filtre_label = ttk.Label(root, text="Filtres :")
filtre_label.place(x=500, y=330)

# Création de la combobox pour le filtre 1
filtre_1_var = tk.StringVar()
filtre_1_combobox = ttk.Combobox(root, textvariable=filtre_1_var, values=["Date", "Type de requete", "Type d'erreur"])
filtre_1_combobox.place(x=500, y=350)

# Création de la combobox pour le filtre 2
filtre_2_var = tk.StringVar()
filtre_2_combobox = ttk.Combobox(root, textvariable=filtre_2_var, values=["Date", "Type de requete", "Type d'erreur"])
filtre_2_combobox.place(x=600, y=350)

def afficher_donnees():
  ...

# Création du tableau
columns = ('ID', 'PACKET ID', 'IP SRC', 'IP DST', 'MAC SRC', 'MAC DST','TYPE TRAME','TIMESTAMP', 'HEURE')
tree = ttk.Treeview(root, columns=columns, show='headings')

# Configurer les en-têtes de colonnes
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)
tree.place(x=20, y=380)  # Positionnez la table à l'emplacement souhaité

# Bouton pour afficher les données dans la table
btn_afficher_donnees = tk.Button(root, text="Afficher les données", command=afficher_donnees)
btn_afficher_donnees.place(x=20, y=340)



# Lancement de l'interface
root.mainloop()
