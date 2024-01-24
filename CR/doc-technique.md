# Description du code
Ce code est une application GUI (Interface Graphique Utilisateur) en utilisant le module Tkinter de Python, le code est basé sur la Programation Orienté au Object, ce qui permet de gagner plus de temps (en appellant les variables partout dans le code) et aussi la propre organisation du code. Il sert pour effectuer une analyse de paquets réseau à l'aide du module script_sniffer, afficher les résultats dans une interface graphique et interagir avec une API REST.

## Partie I
### Modules importés
![Alt text](../images/1.png)

Ces lignes de code sert à importer les modules tkinter, requests, json, et threading. Le module script_sniffer est également importé avec l'alias sniff_packets.

### Definition de Class 'App'
![Alt text](../images/2.png)

Definition d'une classe 'App' héritant de 'tk.Tk' [grace au contenu de ce lien](https://www.pierre-giraud.com/python-apprendre-programmer-cours/oriente-objet-heritage-polymorphisme/).
L'utilisation d'un constructeur (__init__) que initialise la fenêtre principale avec un titre, une taille et appelle deux méthodes (create_widgets et setup_api) pour créer les composants de l'interface graphique et configurer l'API.

## Partie II
### Definition de Methodes (Fonctions)
#### Méthodes pour Afficher des Informations dans l'Interface

Ces méthodes affichent différents types d'informations dans les zones de texte de l'interface (dashboard), comme des messages, des filtres, et des statistiques sur les trames réseau analysées.
- Affichage de Message
![Alt text](../images/3.png)

Cette méthode permet d'afficher un message dans une boîte de texte spécifiée (box_affichage_tests) dans l'interface graphique. Elle commence par autoriser la modification de la boîte de texte, y insère le message à la fin suivi d'un saut de ligne, puis désactive à nouveau la possibilité de modification de la boîte de texte. J'ai utilisé cella pour afficher une message lorsque l'API est connecté ou pas, aussi lorsque le script de scan de paquets est lancé ainsi quand il s'est arreté.

- Affichage de données + filtres
![Alt text](../images/28.png)
![Alt text](../images/29.png)

Ces codes ils sont associées à la gestion d'un tableau (self.tree), généralement utilisé dans l'interface graphique pour afficher des données.

- **1 - ajouter_ligne_tableau(self, trame, rouge=False) :**

Cette méthode prend une trame en entrée et l'ajoute à un tableau (self.tree). Les valeurs de chaque colonne de la ligne sont extraites à partir des propriétés de la trame. Si l'argument optionnel rouge est vrai, une configuration spécifique est appliquée pour indiquer une alerte visuelle dans le tableau.
values : Un tuple contenant les valeurs de chaque colonne de la ligne.

tags : Un tuple vide si rouge est faux, sinon contient le tag "rouge_tableau" pour configurer une couleur différente pour la ligne d'alerte.

La ligne est ensuite ajoutée au tableau avec les valeurs et les tags spécifiés.

Une configuration est ajoutée pour spécifier que les lignes avec le tag "rouge_tableau" doivent avoir une couleur de fond rouge et une couleur de texte blanche.

- **2 - afficher_filtre(self) :**

Cette méthode est liée à la gestion de filtres dans le tableau. Elle efface toutes les lignes existantes dans le tableau, puis filtre les données JSON en fonction de la valeur sélectionnée dans un filtre (selected_filtre). Si un filtre est appliqué, seules les trames correspondant au type de trame sélectionné sont conservées. Ensuite, chaque trame filtrée est ajoutée au tableau en utilisant la méthode ajouter_ligne_tableau avec rouge=False, ce qui signifie qu'aucune alerte n'est indiquée visuellement.

*PS :* Le code assume que le tableau (self.tree) et d'autres éléments associés sont correctement définis dans le contexte global de la classe, car ces méthodes semblent faire référence à des attributs de l'instance de la classe.


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

Utilisation d'une zone de texte pour pouvoir afficher la detenction d'alertes.

- Label

Les labels ça sert pour donner de tittres dans les zones, j'ai utilisé pour m'aider a donner un tittre à cote de combobox de filtrage.
![Alt text](../images/11.png)

- Combobox
![Alt text](../images/12.png)

Ce code crée une combobox avec quatre options ("Request", "nak", "Offer", "ack") dans l'interface. Lorsque l'utilisateur sélectionne une option, la méthode self.afficher_filtre() est appelée pour mettre à jour l'affichage en fonction du filtre sélectionné. La particularité ici c'est l'utilisation de <lambda> que lie un événement à la combobox. Cet événement est déclenché lorsque l'utilisateur sélectionne un élément dans la combobox. Lorsque cet événement se produit, la méthode self.afficher_filtre() est appelée, probablement pour mettre à jour l'affichage en fonction de la nouvelle sélection dans la combobox.

- Boutons
![Alt text](../images/13.png)
![Alt text](../images/16.png)

Ces lignes de code créent des boutons dans l'interface avec différentes fonctions associées. Ces fonctions incluent la fermeture de l'application, l'affichage de statistiques, le démarrage et l'arrêt du scan des paquets DHCP, l'affichage de données dans le tableau et la detenction d'alertes.

- Création de tableau
![Alt text](../images/14.png)

Ces lignes de code crée une structure de tableau dans l'interface avec des colonnes spécifiées, des en-têtes de colonne configurés, et des paramètres de mise en page tels que la position et la largeur des colonnes. Il y a une particularité dans ce code **"for col in columns: ..."**: cette boucle permet de parcourir chaque colonne et configure les en-têtes de colonne avec les noms correspondants. La commande self.trier_colonne(c) est liée à chaque en-tête, indiquant probablement une fonction de tri qui sera appelée lorsqu'un en-tête est cliqué.

#### Méthodes pour Manipuler les Paquets Réseau
![Alt text](../images/16.png)

Globalement, ces méthodes sont liées à la capture de paquets réseau à l'aide de Scapy, l'utilisation en forme de  module permet d'executer le script de sniff que se trouve à l'exterieur. La méthode start_sniffing démarre le scan des paquets de manière synchrone, tandis que start_sniffing_threaded le fait de manière asynchrone en utilisant un thread. La méthode stop_sniffing est utilisée pour arrêter le scan des paquets.

#### Méthodes pour Configurer l'API
![Alt text](../images/18.png)

La méthode setup_api établie une connexion à une API REST via une requête HTTP GET vers l'URL http://localhost:5001/api/elements.

1 - Effectue une requête GET vers l'API REST à l'URL spécifié.

2 - Vérifie si le code d'état de la réponse est égal à 200 (réussite de la requête).

3 - Si la requête est réussie : Stocke le contenu de la réponse dans la variable self.data et affiche un message dans une boîte de texte indiquant que la connexion à l'API REST a été établie avec succès.

4 - Si la requête échoue : Affiche un message dans la boîte de texte indiquant que la connexion a échoué, incluant le code d'état de la réponse.

6 - Désactive la possibilité de modifier le texte dans la boîte de texte.

#### Méthode pour Détecter des Alertes
![Alt text](../images/27.png)

La méthode **detecter_alertes** analyse des trames réseau stockées au format JSON, détecte des alertes en fonction de critères spécifiques sur les adresses IP de destination, et affiche les alertes détectées dans une boîte de texte dédiée. 

Pour chaque trame, l'adresse IP de destination est extraite, et si elle ne correspond pas à certains sous-réseaux spécifiques, une alerte est déclenchée. L'alerte est affichée dans une boîte d'affichage des erreurs en rouge, et une indication visuelle est ajoutée dans un tableau. Les détails des alertes sont également ajoutés à la boîte d'affichage des erreurs, avec une configuration de texte en rouge. En cas d'adresse IP autorisée, une ligne normale est ajoutée dans le tableau. La configuration finale spécifie que le texte avec le tag "rouge" doit avoir une couleur de texte rouge.
Ici le code est focalisé sur la detenction des alertes de paquets DHCP capturés dans des salles 202 et 203.

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









