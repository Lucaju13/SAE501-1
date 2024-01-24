# Documentation Technique de l'API

# Sommaire

1. [Introduction](#introduction)
2. [Prérequis](#prérequis)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Utilisation](#utilisation)
6. [Endpoints](#endpoints)
   - [Exécution du Script](#exécution-du-script)
   - [Obtention de tous les éléments](#obtention-de-tous-les-éléments)
   - [Obtention d'un élément par ID](#obtention-dun-élément-par-id)
   - [Adresses IP destinataires](#adresses-ip-destinataires)
   - [Adresses IP source](#adresses-ip-source)
   - [Capture Time](#capture-time)
   - [Type Trame](#type-trame)
   - [Nombre de Trames par IP Source](#nombre-de-trames-par-ip-source)
   - [Nombre de Trames par IP Destinataire](#nombre-de-trames-par-ip-destinataire)
7. [Conclusion](#conclusion)


## Introduction
Cette documentation fournit des informations détaillées sur l'utilisation de l'API. L'API est construite à l'aide de Flask, et elle expose des fonctionnalités pour exécuter un script, obtenir des informations sur les éléments stockés dans une base de données SQLite, ainsi que des statistiques sur les adresses IP, les temps de capture et le type de trame.

## Prérequis
- Python 3.x installé sur la machine
- Flask et ses dépendances installées (vous pouvez les installer en exécutant `pip install Flask`)

## Installation
1. Téléchargez le script de l'API sur votre machine.
2. Assurez-vous que Python est installé.
3. Installez Flask en exécutant `pip3 install Flask`.

## Configuration
- Le script utilise une base de données SQLite nommée 'sae501.db'.
- Le script suppose que le script 'script_sniffer.py' peut être exécuté avec `sudo python3 script_sniffer.py`.

## Utilisation
- Exécutez le script de l'API `api.py`.
- L'API sera accessible aux adresses spécifiées lors de l’exécution du script.

## Endpoints
1. **Exécution du Script**
   - Endpoint: `/api/run_script`
   - Méthode: GET
   - Description: Exécute le script 'script_sniffer.py'.
   - Réponse réussie: `{'message': 'Script exécuté avec succès'}`

2. **Obtention de tous les éléments**
   - Endpoint: `/api/elements`
   - Méthode: GET
   - Description: Récupère tous les éléments stockés dans la base de données.
   - Réponse réussie: Liste de dictionnaires représentant les éléments.

3. **Obtention d'un élément par ID**
   - Endpoint: `/api/elements/<int:element_id>`
   - Méthode: GET
   - Description: Récupère un élément spécifique en fonction de son ID.
   - Réponse réussie: Dictionnaire représentant l'élément trouvé.

4. **Adresses IP destinataires**
   - Endpoint: `/api/dst_ip`
   - Méthode: GET
   - Description: Récupère toutes les adresses IP destinataires disponibles dans la base de données.
   - Réponse réussie: Liste des adresses IP destinataires.
   - Endpoint: `/api/dst_ip/<ip_dst>`
   - Méthode: GET
   - Description: Récupère des informations sur une adresse IP destinataire spécifique.
   - Réponse réussie: Liste d'informations sur l'adresse IP destinataire.

5. **Adresses IP source**
   - Endpoint: `/api/src_ip`
   - Méthode: GET
   - Description: Récupère toutes les adresses IP source disponibles dans la base de données.
   - Réponse réussie: Liste des adresses IP source.
   - Endpoint: `/api/src_ip/<ip_source>`
   - Méthode: GET
   - Description: Récupère des informations sur une adresse IP source spécifique.
   - Réponse réussie: Liste d'informations sur l'adresse IP source.

6. **Capture Time**
   - Endpoint: `/api/capture_time`
   - Méthode: GET
   - Description: Récupère tous les temps de capture disponibles dans la base de données.
   - Réponse réussie: Liste des temps de capture.

7. **Type Trame**
   - Endpoint: `/api/type_trame`
   - Méthode: GET
   - Description: Récupère des informations sur le type de trame en groupant par adresse IP source.
   - Réponse réussie: Liste d'informations sur le type de trame par adresse IP source.

8. **Nombre de Trames par IP Source**
   - Endpoint: `/api/nombre_trame_par_ip_src`
   - Méthode: GET
   - Description: Récupère le nombre de trames groupées par adresse IP source.
   - Réponse réussie: Liste du nombre de trames par adresse IP source.

9. **Nombre de Trames par IP Destinataire**
   - Endpoint: `/api/nombre_trame_par_ip_dst`
   - Méthode: GET
   - Description: Récupère le nombre de trames groupées par adresse IP destinataire.
   - Réponse réussie: Liste du nombre de trames par adresse IP destinataire.

## Conclusion
Cette documentation fournit une vue d'ensemble des fonctionnalités de l'API, comment la configurer et l'utiliser. Assurez-vous de respecter les prérequis et les configurations nécessaires pour un fonctionnement optimal.
