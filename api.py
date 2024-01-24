from flask import Flask, request, jsonify
import sqlite3
import subprocess

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

# autre ajout de fonction possible selon les routes voulues par les clients

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=False)
