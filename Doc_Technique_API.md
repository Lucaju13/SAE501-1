# Documentation Technique API
## Structure du Code

## Importation des Modules
- Flask: Framework web.
- request: Gestion des requêtes HTTP.
- jsonify: Conversion des données en format JSON.
- sqlite3: Interaction avec la base de données SQLite.
- subprocess: Exécution de scripts Python en tant que processus séparés.

## Configuration de l'Application Flask
- Initialisation d'une instance Flask.

## Fonction de Connexion à la Base de Données SQLite
- Fonction `connect_db()` qui établit une connexion à la base de données SQLite 'sae501.db'.

## Exécution d'un Script avec subprocess
- Route `/api/run_script` (GET) qui exécute le script `script_sniffer.py` avec subprocess.

## Routes pour Obtenir des Éléments depuis la Base de Données
- `/api/elements` (GET) : Récupère tous les éléments.
- `/api/elements/<element_id>` (GET) : Récupère un élément par son ID.

## Routes pour les Adresses IP Destinataires
- `/api/dst_ip` (GET) : Récupère toutes les adresses IP destinataires.
- `/api/dst_ip/<ip_dst>` (GET) : Récupère des informations spécifiques sur une adresse IP destinataire.

## Routes pour les Adresses IP Source
- `/api/src_ip` (GET) : Récupère toutes les adresses IP source.
- `/api/src_ip/<ip_source>` (GET) : Récupère des informations spécifiques sur une adresse IP source.

## Routes pour le Temps de Capture et le Type de Trame
- `/api/capture_time` (GET) : Récupère les moments de capture.
- `/api/type_trame` (GET) : Récupère les types de trame et le nombre associé, regroupés par adresse IP source.

## Routes pour le Nombre de Trames par Adresse IP Source et Destination
- `/api/nombre_trame_par_ip_src` (GET) : Récupère le nombre de trames capturées regroupées par adresse IP source.
- `/api/nombre_trame_par_ip_dst` (GET) : Récupère le nombre de trames capturées regroupées par adresse IP destinataire.

## Exécution de l'Application Flask
- `if __name__ == '__main__': app.run(host='0.0.0.0', port=5000, debug=False)`
