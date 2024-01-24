from flask import Flask, request, jsonify
import sqlite3
import subprocess
import time

app = Flask(__name__)

# Fonction pour se connecter à la base de données SQLite
def connect_db():
    conn = sqlite3.connect('sae501.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/run_script', methods=['GET'])
def run_script():
    try:
        # Exécutez le script en utilisant subprocess
        subprocess.run(['sudo', 'python3', 'script_sniffer.py'])
        return jsonify({'message': 'Script exécuté avec succès'})
    except Exception as e:
        return jsonify({'message': f'Erreur lors de l\'exécution du script: {str(e)}'}), 500
	    
# Route pour obtenir tous les éléments
@app.route('/api/elements', methods=['GET'])
def obtenir_elements():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data")
    elements = cursor.fetchall()
    conn.close()
    elements_dict = [dict(row) for row in elements]
    return jsonify(elements_dict)

# Routes pour obtenir un élément par son ID
@app.route('/api/elements/<int:element_id>', methods=['GET'])
def obtenir_element(element_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data WHERE id=?", (element_id,))
    element = cursor.fetchone()
    conn.close()
    if element:
        return jsonify(dict(element))
    else:
        return jsonify({'message': 'Element non trouve'}), 404

# Route adresses IP destinataires
@app.route('/api/dst_ip', methods=['GET'])
def obtenir_ip_destinataire():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT Dst_ip FROM data")
    ip_destinataire = cursor.fetchall()
    conn.close()
    ip_destinataire_list = [ip[0] for ip in ip_destinataire]
    return jsonify(ip_destinataire_list)
    
@app.route('/api/dst_ip/<ip_dst>', methods=['GET'])
def obtenir_info_ip_dst(ip_dst):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data WHERE Dst_ip = ?", (ip_dst,))
    ip_info = cursor.fetchall()
    conn.close()
    result = [{'type_trame': info[8], 'ip_source': info[1], 'ip_destianaire': info[2]} for info in ip_info]
    return jsonify(result)
    
# Routes adresses IP source
@app.route('/api/src_ip', methods=['GET'])
def obtenir_ip_dst():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT Src_ip FROM data")
    ip_source = cursor.fetchall()
    conn.close()
    ip_source_list = [ip[0] for ip in ip_source]
    return jsonify(ip_source_list)

@app.route('/api/src_ip/<ip_source>', methods=['GET'])
def obtenir_info_ip_src(ip_source):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data WHERE Src_ip = ?", (ip_source,))
    ip_info = cursor.fetchall()
    conn.close()
    result = [{'type_trame': info[8], 'ip_source': info[1], 'ip_destianaire': info[2]} for info in ip_info]
    return jsonify(result)
    
# Route capture time
@app.route('/api/capture_time', methods=['GET'])
def obtenir_capture_time():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT Heure FROM data")
    capture_time = cursor.fetchall()
    conn.close()
    capture_time_list = [ip[0] for ip in capture_time]
    return jsonify(capture_time_list)

# Route Type Trame
@app.route('/api/type_trame', methods=['GET'])
def obtenir_type_trame():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT Type_Trame, Src_ip, COUNT(*) FROM data GROUP BY Type_Trame, Src_ip")
    type_trame_info = cursor.fetchall()
    conn.close()
    result = [{'type_trame': trame[0], 'ip_source': trame[1], 'nombre': trame[2]} for trame in type_trame_info]
    return jsonify(result)

# Type Trame par IP Source
@app.route('/api/nombre_trame_par_ip_src', methods=['GET'])
def obtenir_nombre_trame_par_ip_src():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT Src_ip, COUNT(*) FROM data GROUP BY Src_ip")
    nombre_trame_par_ip_src = cursor.fetchall()
    conn.close()
    result = [{'ip_source': ip[0], 'nombre': ip[1]} for ip in nombre_trame_par_ip_src]
    return jsonify(result)
    
# Type Trame par IP Destinataire
@app.route('/api/nombre_trame_par_ip_dst', methods=['GET'])
def obtenir_nombre_trame_par_ip_dst():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT Dst_ip, COUNT(*) FROM data GROUP BY Dst_ip")
    nombre_trame_par_ip_dst = cursor.fetchall()
    conn.close()
    result = [{'ip_destinataire': ip[0], 'nombre': ip[1]} for ip in nombre_trame_par_ip_dst]
    return jsonify(result)

# Routes adresses MAC destinataire
@app.route('/api/dst_mac', methods=['GET'])
def obtenir_mac_destinataire():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT Dst_mac FROM data")
    mac_destinataire = cursor.fetchall()
    conn.close()
    mac_destinataire_list = [mac[0] for mac in mac_destinataire]
    return jsonify(mac_destinataire_list)

@app.route('/api/dst_mac/<mac_dest>', methods=['GET'])
def obtenir_info_mac_dst(mac_dest):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data WHERE Dst_mac = ?", (mac_dest,))
    mac_info = cursor.fetchall()
    conn.close()
    result = [{'type_trame': info[8], 'mac_source': info[3], 'mac_destinataire': info[4]} for info in mac_info]
    return jsonify(result)

# Routes adresses MAC source
@app.route('/api/src_mac', methods=['GET'])
def obtenir_mac_source():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT Src_mac FROM data")
    mac_source = cursor.fetchall()
    conn.close()
    mac_source_list = [mac[0] for mac in mac_source]
    return jsonify(mac_source_list)

@app.route('/api/src_mac/<mac_src>', methods=['GET'])
def obtenir_info_mac_src(mac_src):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data WHERE Src_mac = ?", (mac_src,))
    mac_info = cursor.fetchall()
    conn.close()
    result = [{'type_trame': info[8], 'mac_source': info[3], 'mac_destinataire': info[4]} for info in mac_info]
    return jsonify(result)

# Route pour compter le nombre de requêtes DHCP de type Discover par Src_mac au cours des dernières 10 secondes
@app.route('/api/request_srcmac', methods=['GET'])
def obtenir_nombre_requetes_dhcp_discover_par_mac_dernieres_10_secondes():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        
        # Calculer le timestamp d'il y a 10 secondes
        temps_actuel = time.time()
        dix_secondes_avant = temps_actuel - 10
        
        # Exécuter une requête pour compter les requêtes DHCP de type Discover par Src_mac au cours des dernières 10 secondes
        cursor.execute("SELECT Src_mac, COUNT(*) FROM data WHERE Type_Trame = 'Discover' AND Time > ? GROUP BY Src_mac", (dix_secondes_avant,))
        nombre_requetes_dhcp_discover_par_mac_dernieres_10_secondes = cursor.fetchall()
        
        conn.close()
        
        # Créer une liste de dictionnaires pour la réponse
        result = [{'mac_source': mac[0], 'nombre': mac[1]} for mac in nombre_requetes_dhcp_discover_par_mac_dernieres_10_secondes]
        
        return jsonify(result)
    except Exception as e:
        return jsonify({'message': f'Erreur : {str(e)}'}), 500

# Route pour répertorier les Src_mac avec plus de 5 requêtes DHCP Discover dans les 10 dernières secondes
@app.route('/api/alerte_discover', methods=['GET'])
def obtenir_src_mac_plus_de_5_requetes_dhcp_discover_dans_10_secondes():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        
        # Calculer le timestamp d'il y a 10 secondes
        temps_actuel = time.time()
        dix_secondes_avant = temps_actuel - 10
        
        # Exécuter une requête pour obtenir les Src_mac avec plus de 5 requêtes DHCP Discover dans les 10 dernières secondes
        cursor.execute("SELECT Src_mac, COUNT(*) as count FROM data WHERE Type_Trame = 'Discover' AND Time > ? GROUP BY Src_mac HAVING count > 5", (dix_secondes_avant,))
        src_mac_plus_de_5_requetes_dhcp_discover_dans_10_secondes = cursor.fetchall()
        
        conn.close()
        
        # Créer une liste de dictionnaires pour la réponse
        result = [{'mac_source': mac[0], 'nombre_requetes_dhcp_discover': mac[1]} for mac in src_mac_plus_de_5_requetes_dhcp_discover_dans_10_secondes]
        
        return jsonify(result)
    except Exception as e:
        return jsonify({'message': f'Erreur : {str(e)}'}), 500

# Route pour afficher les trames concernant deux adresses MAC spécifiques
@app.route('/api/trame_combinee/<mac_source>/<mac_dest>', methods=['GET'])
def obtenir_trames_entre_deux_mac(mac_source, mac_dest):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # Exécuter une requête pour obtenir les trames entre deux adresses MAC spécifiques
        cursor.execute("SELECT * FROM data WHERE Src_mac = ? AND Dst_mac = ?", (mac_source, mac_dest))
        trames_entre_deux_mac = cursor.fetchall()

        conn.close()

        # Créer une liste de dictionnaires pour la réponse
        result = [{'type_trame': trame[8], 'mac_source': trame[3], 'mac_destinataire': trame[4]} for trame in trames_entre_deux_mac]

        return jsonify(result)
    except Exception as e:
        return jsonify({'message': f'Erreur : {str(e)}'}), 500

# autre ajout de fonction possible selon les routes voulues par les clients

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=False)
