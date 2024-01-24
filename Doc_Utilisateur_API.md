# Documentation Utilisateur API
## Application de Surveillance Réseau

Bienvenue dans l'application de surveillance réseau basée sur Flask. Cette application vous permet d'explorer les données de capture réseau stockées dans une base de données SQLite. Voici comment vous pouvez utiliser les fonctionnalités disponibles.

L'api est accessible sur les adresses :

- http://localhost:5000/"endpoints" (depuis le raspberry)
- http://"@IP raspberry":5000/"endpoints" (depuis les autres machines sur le réseau)
## Exécuter le Script de Capture

- **Endpoint:** `/api/run_script` (GET)
- **Description:** Cette fonctionnalité vous permet d'exécuter un script de capture réseau. Cela peut être utile pour mettre à jour les données de capture en temps réel.
- **Comment Utiliser :** Effectuez une requête GET à l'endpoint `/api/run_script`. Assurez-vous d'avoir les autorisations nécessaires, car l'exécution de scripts peut nécessiter des privilèges.

## Obtenir Tous les Éléments Capturés

- **Endpoint:** `/api/elements` (GET)
- **Description:** Récupère tous les éléments capturés dans la base de données.
- **Comment Utiliser :** Effectuez une requête GET à l'endpoint `/api/elements`.

## Obtenir un Élément par son ID

- **Endpoint:** `/api/elements/<element_id>` (GET)
- **Description:** Récupère un élément spécifique en fonction de son ID.
- **Comment Utiliser :** Remplacez `<element_id>` par l'ID réel de l'élément que vous souhaitez obtenir. Effectuez une requête GET à cet endpoint.

## Obtenir les Adresses IP Destinataires

- **Endpoint:** `/api/dst_ip` (GET)
- **Description:** Récupère toutes les adresses IP destinataires présentes dans les données capturées.
- **Comment Utiliser :** Effectuez une requête GET à l'endpoint `/api/dst_ip`.

## Obtenir des Informations sur une Adresse IP Destinataire

- **Endpoint:** `/api/dst_ip/<ip_dst>` (GET)
- **Description:** Récupère des informations spécifiques sur une adresse IP destinataire donnée.
- **Comment Utiliser :** Remplacez `<ip_dst>` par l'adresse IP destinataire réelle que vous souhaitez explorer. Effectuez une requête GET à cet endpoint.

## Obtenir les Adresses IP Source

- **Endpoint:** `/api/src_ip` (GET)
- **Description:** Récupère toutes les adresses IP source présentes dans les données capturées.
- **Comment Utiliser :** Effectuez une requête GET à l'endpoint `/api/src_ip`.

## Obtenir des Informations sur une Adresse IP Source

- **Endpoint:** `/api/src_ip/<ip_source>` (GET)
- **Description:** Récupère des informations spécifiques sur une adresse IP source donnée.
- **Comment Utiliser :** Remplacez `<ip_source>` par l'adresse IP source réelle que vous souhaitez explorer. Effectuez une requête GET à cet endpoint.

## Obtenir les Moments de Capture

- **Endpoint:** `/api/capture_time` (GET)
- **Description:** Récupère les moments de capture associés aux données capturées.
- **Comment Utiliser :** Effectuez une requête GET à l'endpoint `/api/capture_time`.

## Obtenir les Types de Trame par Adresse IP Source

- **Endpoint:** `/api/type_trame` (GET)
- **Description:** Récupère les types de trame et le nombre associé, regroupés par adresse IP source.
- **Comment Utiliser :** Effectuez une requête GET à l'endpoint `/api/type_trame`.

## Obtenir le Nombre de Trames par Adresse IP Source

- **Endpoint:** `/api/nombre_trame_par_ip_src` (GET)
- **Description:** Récupère le nombre de trames capturées regroupées par adresse IP source.
- **Comment Utiliser :** Effectuez une requête GET à l'endpoint `/api/nombre_trame_par_ip_src`.

## Obtenir le Nombre de Trames par Adresse IP Destinataire

- **Endpoint:** `/api/nombre_trame_par_ip_dst` (GET)
- **Description:** Récupère le nombre de trames capturées regroupées par adresse IP destinataire.
- **Comment Utiliser :** Effectuez une requête GET à l'endpoint `/api/nombre_trame_par_ip_dst`.
