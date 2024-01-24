# Description du code
Ce code est une application GUI (Interface Graphique Utilisateur) en utilisant le module Tkinter de Python, le code est basé sur la Programation Orienté au Object, ce qui m'a permis de gagner plus de temps (en appellant les variables partout dans le code) et aussi la propre organisation du code. Il sert pour effectuer une analyse de paquets réseau à l'aide du module script_sniffer, afficher les résultats dans une interface graphique et interagir avec une API REST.

## Partie I
### Modules importés
![Alt text](../images/1.png)

J'ai importé les modules tkinter, requests, json, et threading. Le module script_sniffer est également importé avec l'alias sniff_packets.

### Definition de Class 'App'
![Alt text](../images/2.png)

J'ai defini une classe 'App' héritant de 'tk.Tk' [grace au contenu de ce lien](https://www.pierre-giraud.com/python-apprendre-programmer-cours/oriente-objet-heritage-polymorphisme/).
Ensuite j'ai utilisé un constructeur (__init__) que initialise la fenêtre principale avec un titre, une taille et appelle deux méthodes (create_widgets et setup_api) pour créer les composants de l'interface graphique et configurer l'API.

## Partie II
### Definition de Methodes (Fonctions)
#### Méthodes pour Afficher des Informations dans l'Interface

Ces méthodes affichent différents types d'informations dans les zones de texte de l'interface (dashboard), comme des messages, des filtres, et des statistiques sur les trames réseau analysées.
- Affichage de Message
![Alt text](../images/3.png)

Cette méthode permet d'afficher un message dans une boîte de texte spécifiée (box_affichage_tests) dans l'interface graphique. Elle commence par autoriser la modification de la boîte de texte, y insère le message à la fin suivi d'un saut de ligne, puis désactive à nouveau la possibilité de modification de la boîte de texte. J'ai utilisé cella pour afficher une message lorsque l'API est connecté ou pas, aussi lorsque le script de scan de paquets est lancé ainsi quand il s'est arreté.

- Affichage de données + filtres
![Alt text](../images/8.png)

J'ai utilisée cette méthode pour filtrer et afficher des données JSON reçues àpartir de l'API Rest dans la structure d'interface utilisateur Tkinter (Treeview). Elle nettoie d'abord la structure, puis filtre les données en fonction de la valeur du filtre sélectionné, et enfin insère les données filtrées dans la structure d'interface utilisateur.

1 - selected_filtre = self.filtre_2_var.get(): Il récupère la valeur actuelle du filtre sélectionné à partir d'une variable Tkinter (filtre_2_var).

2 - self.parse_json = json.loads(self.data): Cette ligne sert à charger les données JSON stockées dans la variable self.data en utilisant la fonction loads du module json. Cela suppose que self.data contient une chaîne JSON valide.

3 - for row in self.tree.get_children(): self.tree.delete(row): Nettoie toutes les lignes actuellement présentes dans la structure d'interface utilisateur (Treeview) pour s'assurer qu'elle est vide avant d'afficher les données filtrées.

4 - if selected_filtre: filtered_data = [trame for trame in self.parse_json if trame.get('Type_Trame', '') == selected_filtre]: Si un filtre est sélectionné, crée une liste appelée filtered_data qui contient uniquement les éléments de self.parse_json dont la clé 'Type_Trame' est égale à la valeur du filtre sélectionné. Sinon, filtered_data est égal à l'ensemble complet de données self.parse_json.

5 - for row in filtered_data: ...: Parcours chaque élément de filtered_data et extrait les valeurs associées aux clés spécifiques ('ID', 'Src_IP', etc.). Ces valeurs sont ensuite insérées dans la structure d'interface utilisateur (Treeview) à la fin de la liste, créant ainsi une nouvelle ligne avec les données filtrées.

- Affichage de statistiques 
![Alt text](../images/9.png)

Cette méthode affiche des statistiques sur le nombre de trames par type dans la boite de texte (Dashboard). Elle nettoie d'abord la boîte de texte, analyse les données JSON pour compter le nombre de trames par type, affiche ces statistiques dans la boîte de texte, puis affiche le nombre total de trames.

1 - self.box_affichage_tests.config(state="normal"): Cette ligne configure l'état de la boîte de texte box_affichage_tests en "normal", permettant ainsi la modification du texte.

2- self.box_affichage_tests.delete(1.0, tk.END): Supprime tout le contenu actuel de la boîte de texte. Cela est fait pour nettoyer la boîte avant d'afficher de nouvelles statistiques.

3 - self.parse_json = json.loads(self.data): Charge les données JSON stockées dans la variable self.data en utilisant json.loads() pour les transformer en une structure Python (probablement une liste de dictionnaires).

4 - Crée un dictionnaire type_count pour stocker le nombre de trames par type.

5 - Parcourt chaque trame dans self.parse_json et compte le nombre de trames par type en utilisant le dictionnaire type_count.

6 - Calcule le nombre total de requêtes en sommant les valeurs du dictionnaire type_count.

7 - Parcourt le dictionnaire type_count et insère chaque type de trame avec son nombre correspondant dans la boîte de texte.

8 - Ajoute une ligne vide dans la boîte de texte.

9 - Ajoute une ligne indiquant le nombre total de trames.

10 - self.box_affichage_tests.config(state="disabled"): Configure à nouveau l'état de la boîte de texte en "disabled", ce qui signifie que le texte ne peut plus être modifié. Cela est souvent utilisé pour empêcher l'utilisateur d'éditer le contenu de la boîte de texte.

#### Méthode create_widgets
Cette méthode crée et place tous les widgets (éléments graphiques) dans la fenêtre. Cela inclut des boutons, des zones de texte, des combobox, et un tableau (Treeview) pour afficher des données.
 - Zone de text (Dashboard)
![Alt text](../images/7.png)

- Zone de text pour la detenction d'alertes
![Alt text](../images/10.png)

J'ai utilisé une zone de texte pour pouvoir afficher la detenction d'alertes.

- Label

Ça m'a servi pour donner de tittres dans les zones, j'ai utilisé pour m'aider a donner un tittre à cote de combobox de filtrage.
![Alt text](../images/11.png)

- Combobox
![Alt text](../images/12.png)

Ce code crée une combobox avec quatre options ("Request", "nak", "Offer", "ack") dans l'interface. Lorsque l'utilisateur sélectionne une option, la méthode self.afficher_filtre() est appelée pour mettre à jour l'affichage en fonction du filtre sélectionné. La particularité ici c'est que j'ai utilisé <lambda> que lie un événement à la combobox. Cet événement est déclenché lorsque l'utilisateur sélectionne un élément dans la combobox. Lorsque cet événement se produit, la méthode self.afficher_filtre() est appelée, probablement pour mettre à jour l'affichage en fonction de la nouvelle sélection dans la combobox.

- Boutons
![Alt text](../images/13.png)
![Alt text](../images/16.png)

Ces lignes de code créent des boutons dans l'interface avec différentes fonctions associées. Ces fonctions incluent la fermeture de l'application, l'affichage de statistiques, le démarrage et l'arrêt du scan des paquets DHCP, l'affichage de données dans le tableau et la detenction d'alertes.

- Création de tableau
![Alt text](../images/14.png)

Dans cette partie j'ai crée une structure de tableau dans l'interface avec des colonnes spécifiées, des en-têtes de colonne configurés, et des paramètres de mise en page tels que la position et la largeur des colonnes. Il y a une particularité dans ce code **"for col in columns: ..."**: cette boucle permet de parcourir chaque colonne et configure les en-têtes de colonne avec les noms correspondants. La commande self.trier_colonne(c) est liée à chaque en-tête, indiquant probablement une fonction de tri qui sera appelée lorsqu'un en-tête est cliqué.

#### Méthodes pour Manipuler les Paquets Réseau
![Alt text](../images/16.png)

Globalement, ces méthodes sont liées à la capture de paquets réseau à l'aide de Scapy, j'ai utilisé en forme de  module pour pouvoir executer le script de sniff que se trouve à l'exterieur. La méthode start_sniffing démarre le scan des paquets de manière synchrone, tandis que start_sniffing_threaded le fait de manière asynchrone en utilisant un thread. La méthode stop_sniffing est utilisée pour arrêter le scan des paquets.

#### Méthodes pour Configurer l'API
![Alt text](../images/18.png)

La méthode setup_api établie une connexion à une API REST via une requête HTTP GET vers l'URL http://localhost:5001/api/elements.

1 - Effectue une requête GET vers l'API REST à l'URL spécifié.

2 - Vérifie si le code d'état de la réponse est égal à 200 (réussite de la requête).

3 - Si la requête est réussie : Stocke le contenu de la réponse dans la variable self.data et affiche un message dans une boîte de texte indiquant que la connexion à l'API REST a été établie avec succès.

4 - Si la requête échoue : Affiche un message dans la boîte de texte indiquant que la connexion a échoué, incluant le code d'état de la réponse.

6 - Désactive la possibilité de modifier le texte dans la boîte de texte.

#### Méthode pour Détecter des Alertes
![Alt text](../images/19.png)

La méthode **detecter_alertes** analyse des trames réseau stockées au format JSON, détecte des alertes en fonction de critères spécifiques sur les adresses IP de destination, et affiche les alertes détectées dans une boîte de texte dédiée. D'abord ce code: 
1 - Efface le contenu actuel de la boîte de texte dédiée aux alertes.

2 - Charge les données JSON en une structure Python.

3 - Parcourt chaque trame dans les données JSON.

4 - Vérifie si l'adresse IP de destination de la trame n'appartient pas à certains sous-réseaux autorisés.

5 - Si une alerte est détectée, construit un message d'alerte.

6 - Insère le message d'alerte dans la boîte de texte avec un style rouge.

7 - Désactive la possibilité de modifier le texte dans la boîte de texte.

Ici j'ai me focalisé sur la detenction des alertes de paquets DHCP capturés dans des salles 202 et 203.

#### Méthode pour Trier les Colonnes du Tableau
![Alt text](../images/20.png)

La méthode **trier_colonne** sert a trier les éléments du tableau crée au-dessus, en fonction de la colonne sur laquelle l'utilisateur a cliqué.
1 - Récupère toutes les valeurs de la colonne spécifiée pour chaque élément du tableau, ainsi que les identifiants correspondants.

2 - Crée une liste de tuples, chaque tuple contenant la valeur de la colonne et l'identifiant de l'élément.

3 - Trie cette liste en fonction des valeurs de la colonne.

4 - Réorganise les éléments du tableau dans l'ordre trié en utilisant la méthode move du tableau.

#### Boucle Principale
![Alt text](../images/21.png)

Ces lignes de code créent une instance de la classe App et exécutent la boucle principale de l'interface graphique Tkinter pour démarrer l'application lorsque le script est exécuté directement.









