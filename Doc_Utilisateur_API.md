# Documentation Utilisateur API
## Application de Surveillance Réseau

# Documentation Utilisateur

## API - Application de Surveillance Réseau

Bienvenue dans l'application de surveillance réseau basée sur Flask. Cette application vous permet d'explorer les données de capture réseau stockées dans une base de données SQLite. Voici comment vous pouvez utiliser les fonctionnalités disponibles.

L'API est accessible sur les adresses :
- http://localhost:5000/ "endpoints" (depuis le Raspberry)
- http://@IP_raspberry:5000/"endpoints" (depuis les autres machines sur le réseau)

**IMPORTANT** - Vérifiez que les fichiers **"script_sniffer.py"**, **"test_unitaire_api.py"**, **"sae501.db"**, et **"api.py"** soient dans le même dossier.


## Exécuter le script de capture

- **Endpoint:** /api/run_script (GET)
- **Description:** Cette fonctionnalité vous permet d'exécuter un script de capture réseau. Cela peut être utile pour mettre à jour les données de capture en temps réel.
- **Comment utiliser :** Recherchez [http://localhost:5000/api/run_script](http://localhost:5000/api/run_script).


## Obtenir tous les éléments capturés

- **Endpoint:** /api/elements (GET)
- **Description:** Récupère tous les éléments capturés dans la base de données.
- **Comment utiliser :** Recherchez [http://localhost:5000/api/elements](http://localhost:5000/api/elements).


## Obtenir un élément par son ID

- **Endpoint:** /api/elements/<element_id> (GET)
- **Description:** Récupère un élément spécifique en fonction de son ID.
- **Comment utiliser :** Remplacez `<element_id>` par l'ID réel de l'élément que vous souhaitez obtenir. Recherchez http://localhost:5000/api/elements/<element_id>


## Obtenir les adresses IP Destinataires

- **Endpoint:** /api/dst_ip (GET)
- **Description:** Récupère toutes les adresses IP destinataires présentes dans les données capturées.
- **Comment utiliser :** Recherchez [http://localhost:5000/api/dst_ip](http://localhost:5000/api/dst_ip).


## Obtenir des informations sur une adresse IP Destinataire

- **Endpoint:** /api/dst_ip/<ip_dst> (GET)
- **Description:** Récupère des informations spécifiques sur une adresse IP destinataire donnée.
- **Comment utiliser :** Remplacez `<ip_dst>` par l'adresse IP destinataire réelle que vous souhaitez explorer. Recherchez http://localhost:5000/api/dst_ip/<ip_dst>


## Obtenir les adresses IP Source

- **Endpoint:** /api/src_ip (GET)
- **Description:** Récupère toutes les adresses IP source présentes dans les données capturées.
- **Comment utiliser :** Recherchez [http://localhost:5000/api/src_ip](http://localhost:5000/api/src_ip).


## Obtenir des informations sur une adresse IP Source

- **Endpoint:** /api/src_ip/<ip_source> (GET)
- **Description:** Récupère des informations spécifiques sur une adresse IP source donnée.
- **Comment utiliser :** Remplacez `<ip_source>` par l'adresse IP source réelle que vous souhaitez explorer. Recherchez http://localhost:5000/api/src_ip/<ip_source>


## Obtenir les moments de capture

- **Endpoint:** /api/capture_time (GET)
- **Description:** Récupère les moments de capture associés aux données capturées.
- **Comment utiliser :** Recherchez [http://localhost:5000/api/capture_time](http://localhost:5000/api/capture_time).


## Obtenir les types de trame par adresse IP Source

- **Endpoint:** /api/type_trame (GET)
- **Description:** Récupère les types de trame et le nombre associé, regroupés par adresse IP source.
- **Comment utiliser :** Recherchez [http://localhost:5000/api/type_trame](http://localhost:5000/api/type_trame).


## Obtenir le nombre de trames par adresse IP Source

- **Endpoint:** /api/nombre_trame_par_ip_src (GET)
- **Description:** Récupère le nombre de trames capturées regroupées par adresse IP source.
- **Comment utiliser :** Recherchez [http://localhost:5000/api/nombre_trame_par_ip_src](http://localhost:5000/api/nombre_trame_par_ip_src).


## Obtenir le nombre de trames par adresse IP Destinataire

- **Endpoint:** /api/nombre_trame_par_ip_dst (GET)
- **Description:** Récupère le nombre de trames capturées regroupées par adresse IP destinataire.
- **Comment utiliser :** Recherchez [http://localhost:5000/api/nombre_trame_par_ip_dst](http://localhost:5000/api/nombre_trame_par_ip_dst).


## Obtenir des informations sur une adresse MAC destinataire

- **Endpoint:** /api/dst_mac (GET)
- **Description:** Récupère toutes les adresses MAC de destination uniques de la table data.
- **Comment utiliser:** Recherchez [http://localhost:5000/api/dst_mac](http://localhost:5000/api/dst_mac).


## Obtenir des informations spécifiques sur une adresse MAC destinataire

- **Endpoint:** /api/dst_mac/<mac_dest> (GET)
- **Description:** Récupère des informations sur les trames associées à une adresse MAC de destination spécifique.
- **Comment utiliser:** Remplacez `<mac_dest>` par l'adresse MAC de destination réelle que vous souhaitez explorer. Recherchez http://localhost:5000/api/dst_mac/<mac_dest>


## Obtenir des adresses MAC source

- **Endpoint:** /api/src_mac (GET)
- **Description:** Récupère toutes les adresses MAC source uniques de la table data.
- **Comment utiliser:** Recherchez [http://localhost:5000/api/src_mac](http://localhost:5000/api/src_mac) pour obtenir la liste des adresses MAC source.


## Obtenir des informations spécifiques sur une adresse MAC source

- **Endpoint:** /api/src_mac/<mac_src> (GET)
- **Description:** Récupère des informations sur les trames associées à une adresse MAC source spécifique.
- **Comment utiliser:** Remplacez `<mac_src>` par l'adresse MAC source réelle que vous souhaitez explorer. Recherchez http://localhost:5000/api/src_mac/<mac_src>


## Obtenir le nombre de requêtes DHCP Discover par adresse MAC source dans les 10 dernières secondes

- **Endpoint:** /api/request_srcmac (GET)
- **Description:** Récupère le nombre de requêtes DHCP Discover par adresse MAC source au cours des dernières 10 secondes.
- **Comment utiliser:** Recherchez [http://localhost:5000/api/request_srcmac](http://localhost:5000/api/request_srcmac).


## Obtenir les adresses MAC source avec plus de 5 requêtes DHCP Discover dans les 10 dernières secondes

- **Endpoint:** /api/alerte_discover (GET)
- **Description:** Récupère les adresses MAC source avec plus de 5 requêtes DHCP Discover dans les 10 dernières secondes.
- **Comment utiliser:** Recherchez [http://localhost:5000/api/alerte_discover](http://localhost:5000/api/alerte_discover).


## Exécution de l'API

L'API peut être exécutée avec la commande `sudo python3 api.py`.
