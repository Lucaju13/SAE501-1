# Description du code
Ce code est une application GUI (Interface Graphique Utilisateur) en utilisant le module Tkinter de Python, le code est basé sur la Programation Orienté au Object, ce qui m'a permis de gagner plus de temps (en appellant les variables partout dans le code) et aussi la propre organisation du code. Il sert pour effectuer une analyse de paquets réseau à l'aide du module script_sniffer, afficher les résultats dans une interface graphique et interagir avec une API REST.

## Partie I
### Modules importés
![Alt text](../images/1.png)
- J'ai importé les modules tkinter, requests, json, et threading. Le module script_sniffer est également importé avec l'alias sniff_packets.

### Definition de Class 'App'
![Alt text](../images/2.png)
- J'ai defini une classe 'App' héritant de 'tk.Tk' [grace au contenu de ce lien](https://www.pierre-giraud.com/python-apprendre-programmer-cours/oriente-objet-heritage-polymorphisme/).
Ensuite j'ai utilisé un constructeur (__init__) que initialise la fenêtre principale avec un titre, une taille et appelle deux méthodes (create_widgets et setup_api) pour créer les composants de l'interface graphique et configurer l'API.

## Partie II
### Definition de Methodes (Fonctions)
- Méthodes pour Afficher des Informations dans l'Interface

Ces méthodes affichent différents types d'informations dans les zones de texte de l'interface, comme des messages, des filtres, et des statistiques sur les trames réseau analysées.
![Alt text](../images/3.png)

Cette méthode permet d'afficher un message dans une boîte de texte spécifiée (box_affichage_tests) dans l'interface graphique. Elle commence par autoriser la modification de la boîte de texte, y insère le message à la fin suivi d'un saut de ligne, puis désactive à nouveau la possibilité de modification de la boîte de texte. J'ai utilisé cella pour afficher une message lorsque l'API est connecté ou pas, aussi lorsque le script de scan de paquets est lancé ainsi quand il s'est arreté.
![Alt text](../images/8.png)
![Alt text](../images/9.png)


-
-
-
-
-



