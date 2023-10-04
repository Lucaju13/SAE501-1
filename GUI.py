import tkinter as tk

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
hauteur = 550
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


# Box d'affichage des données stockées dans la base de données
bdaf = tk.Label(root, text="Base de Données")
bdaf.place(x = 0, y= 330)
box_affichage_db = tk.Text(root, height=10, width=50)
box_affichage_db.place(x=0, y= 350)

# Lancement de l'interface
root.mainloop()
