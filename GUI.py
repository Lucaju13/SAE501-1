import tkinter as tk

def lancer_requete():
    # Ajoutez ici le code pour lancer la requête
    pass

def sauvegarder():
    # Ajoutez ici le code pour sauvegarder dans la base de données
    pass

# Création de la fenêtre principale
root = tk.Tk()
root.title("Interface")

# Box pour prendre l’adresse API REST
api = tk.Label(root, text= "API REST URL")
api.pack()
box_adresse_api = tk.Entry(root, width=50)
box_adresse_api.pack()

# Box d'affichage des résultats de Test Unitaires
test_unitaires = tk.Label(root, text="Résultat tests unitaires")
test_unitaires.pack()
box_affichage_tests = tk.Text(root, height=10, width=50)
box_affichage_tests.pack()

# Box d'affichage des erreurs
erreurs = tk.Label(root, text="Affichage des erreurs")
erreurs.pack()
box_affichage_erreurs = tk.Text(root, height=10, width=50)
box_affichage_erreurs.pack()

# Boutons
btn_lancer_requete = tk.Button(root, text="Lancer la requête", command=lancer_requete)
btn_lancer_requete.pack()

btn_sortir = tk.Button(root, text="Sortir du programme", command=root.quit)
btn_sortir.pack()

btn_stop = tk.Button(root, text="Stop", command=root.quit)  # Ajoutez la fonction associée
btn_stop.pack()

btn_sauvegarder = tk.Button(root, text="Sauvegarder", command=sauvegarder)
btn_sauvegarder.pack()

# Filtres
filtres_label = tk.Label(root, text="Filtres")
filtres_label.pack()

filtre_date = tk.Entry(root)
filtre_date.pack()

filtre_type_requete = tk.Entry(root)
filtre_type_requete.pack()

filtre_type_erreur = tk.Entry(root)
filtre_type_erreur.pack()

# Détection des alertes
alertes_label = tk.Label(root, text="Détection des alertes")
alertes_label.pack()

alertes_button = tk.Button(root, text="Chercher anomalies DHCP")  # Ajoutez la fonction associée
alertes_button.pack()

# Box d'affichage des données stockées dans la base de données
bdaf = tk.Label(root, text="Base de Données")
bdaf.pack()
box_affichage_db = tk.Text(root, height=10, width=50)
box_affichage_db.pack()

# Lancement de l'interface
root.mainloop()
