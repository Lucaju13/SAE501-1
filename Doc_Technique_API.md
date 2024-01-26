# Documentation Technique de l'API REST Flask

## Introduction
Cette documentation technique fournit des informations détaillées sur l'API REST Flask développée en Python. L'API permet d'interagir avec une base de données SQLite, d'exécuter un script, et de fournir diverses informations liées aux trames réseau capturées.

## Fonctionnement Général
L'API présente plusieurs endpoints permettant de récupérer des informations à partir de la base de données SQLite, d'exécuter un script externe, et d'effectuer des opérations de requêtes.

## Prérequis
- **Python 3.x**: L'API est développée en Python 3.
- **Flask**: Le framework Flask est utilisé pour créer l'API REST.
- **Flask-SSLify**: Cette extension assure que toutes les connexions sont redirigées vers HTTPS.
- **SQLite3**: La base de données utilisée par l'API est SQLite3.
- **Subprocess**: La bibliothèque Subprocess est utilisée pour exécuter des scripts externes.

## Structure du Projet
- **script_sniffer.py**: Effectue une capture de trame en direct.
- **test_unitaire_api.py**: Vérifie le bon fonctionnement de l'API et ne lance pas l’API si un des tests n’est pas bon.

## Configuration
L'API est configurée pour fonctionner avec une base de données SQLite nommée `sae501.db`.

## Endpoints de l'API

### 1. **/api/run_script (GET)**
- **Description**: Exécute le script externe `script_sniffer.py`.
- **Réponse**: Retourne un message indiquant si le script a été exécuté avec succès ou s'il y a eu une erreur.

### 2. **/api/elements (GET)**
- **Description**: Récupère tous les éléments de la table `data` de la base de données.
- **Réponse**: Retourne une liste d'éléments sous forme de dictionnaires.

### 3. **/api/elements/<int:element_id> (GET)**
- **Description**: Récupère un élément spécifique par son ID dans la table `data`.
- **Réponse**: Retourne un dictionnaire représentant l'élément trouvé ou un message si l'élément n'est pas trouvé.

### 4. **/api/dst_ip (GET)**
- **Description**: Récupère toutes les adresses IP de destination uniques de la table `data`.
- **Réponse**: Retourne une liste d'adresses IP de destination.

### 5. **/api/dst_ip/<ip_dst> (GET)**
- **Description**: Récupère des informations sur les trames associées à une adresse IP de destination spécifique.
- **Réponse**: Retourne une liste de dictionnaires représentant les informations sur les trames.

### 6. **/api/src_ip (GET)**
- **Description**: Récupère toutes les adresses IP source uniques de la table `data`.
- **Réponse**: Retourne une liste d'adresses IP source.

### 7. **/api/src_ip/<ip_source> (GET)**
- **Description**: Récupère des informations sur les trames associées à une adresse IP source spécifique.
- **Réponse**: Retourne une liste de dictionnaires représentant les informations sur les trames.

### 8. **/api/capture_time (GET)**
- **Description**: Récupère toutes les heures de capture de la table `data`.
- **Réponse**: Retourne une liste d'heures de capture.

### 9. **/api/type_trame (GET)**
- **Description**: Récupère le nombre de trames groupées par type et adresse IP source.
- **Réponse**: Retourne une liste de dictionnaires représentant les informations sur le type de trame, l'adresse IP source et le nombre de trames.

### 10. **/api/nombre_trame_par_ip_src (GET)**
- **Description**: Récupère le nombre de trames groupées par adresse IP source.
- **Réponse**: Retourne une liste de dictionnaires représentant l'adresse IP source et le nombre de trames.

### 11. **/api/nombre_trame_par_ip_dst (GET)**
- **Description**: Récupère le nombre de trames groupées par adresse IP destination.
- **Réponse**: Retourne une liste de dictionnaires représentant l'adresse IP destination et le nombre de trames.

### 12. **/api/dst_mac (GET)**
- **Description**: Récupère toutes les adresses MAC de destination uniques de la table `data`.
- **Réponse**: Retourne une liste d'adresses MAC de destination.

### 13. **/api/dst_mac/<mac_dest> (GET)**
- **Description**: Récupère des informations sur les trames associées à une adresse MAC de destination spécifique.
- **Réponse**: Retourne une liste de dictionnaires représentant les informations sur les trames.

### 14. **/api/src_mac (GET)**
- **Description**: Récupère toutes les adresses MAC source uniques de la table `data`.
- **Réponse**: Retourne une liste d'adresses MAC source.

### 15. **/api/src_mac/<mac_src> (GET)**
- **Description**: Récupère des informations sur les trames associées à une adresse MAC source spécifique.
- **Réponse**: Retourne une liste de dictionnaires représentant les informations sur les trames.

### 16. **/api/request_srcmac (GET)**
- **Description**: Récupère le nombre de requêtes DHCP Discover par adresse MAC source au cours des dernières 10 secondes.
- **Réponse**: Retourne une liste de dictionnaires représentant l'adresse MAC source et le nombre de requêtes.

### 17. **/api/alerte_discover (GET)**
- **Description**: Récupère les adresses MAC source avec plus de 5 requêtes DHCP Discover dans les 10 dernières secondes.
- **Réponse**: Retourne une liste de dictionnaires représentant l'adresse MAC source et le nombre de requêtes DHCP Discover.

### 18. **/api/trame_combinee/<mac_source>/<mac_dest> (GET)**
- **Description**: Récupère les trames entre deux adresses MAC spécifiques.
- **Réponse**: Retourne une liste de dictionnaires représentant les informations sur les trames.

## Exécution de l'API
L'API peut être exécutée en exécutant le script principal `api.py` avec la commande `sudo python3 api.py`. L'API sera accessible sur [http://localhost:5000/](http://localhost:5000/) depuis la machine hôte et depuis les autres machines sur [http://<IP_machine_hôte>:5000/](http://<IP_machine_hôte>:5000/).
