from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Fonction pour se connecter à la base de données SQLite
def connect_db():
    conn = sqlite3.connect('sae501.db')
    conn.row_factory = sqlite3.Row
    return conn

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

# Route pour obtenir un élément par son ID
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

# Route pour obtenir toutes les adresses IP destinataires
@app.route('/api/dst_ip', methods=['GET'])
def obtenir_ip_destinataire():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT Dst_ip FROM data")
    ip_destinataire = cursor.fetchall()
    conn.close()
    ip_destinataire_list = [ip[0] for ip in ip_destinataire]
    return jsonify(ip_destinataire_list)

# Route pour obtenir toutes les adresses IP source
@app.route('/api/src_ip', methods=['GET'])
def obtenir_ip_source():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT Src_ip FROM data")
    ip_source = cursor.fetchall()
    conn.close()
    ip_source_list = [ip[0] for ip in ip_source]
    return jsonify(ip_source_list)
    
@app.route('/api/capture_time', methods=['GET'])
def obtenir_capture_time():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT Heure FROM data")
    ip_destinataire = cursor.fetchall()
    conn.close()
    ip_destinataire_list = [ip[0] for ip in ip_destinataire]
    return jsonify(ip_destinataire_list)

@app.route('/api/type_trame', methods=['GET'])
def obtenir_type_trame():
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT Type_Trame, Src_ip, COUNT(*) FROM data GROUP BY Type_Trame, Src_ip")
    
    type_trame_info = cursor.fetchall()
    
    conn.close()
    
    result = [{'type_trame': trame[0], 'ip_source': trame[1], 'nombre': trame[2]} for trame in type_trame_info]
    
    return jsonify(result)

@app.route('/api/nombre_trame_par_ip', methods=['GET'])
def obtenir_nombre_trame_par_ip():
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT Src_ip, COUNT(*) FROM data GROUP BY Src_ip")
    
    nombre_trame_par_ip = cursor.fetchall()
    
    conn.close()
    
    result = [{'ip_source': ip[0], 'nombre': ip[1]} for ip in nombre_trame_par_ip]
    
    return jsonify(result)
    
@app.route('/api/src_ip/<ip_source>', methods=['GET'])
def obtenir_info_ip(ip_source):
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM data WHERE Src_ip = ?", (ip_source,))
    
    ip_info = cursor.fetchall()
    
    conn.close()
    
    result = [{'type_trame': info[8], 'ip_source': info[1], 'ip_destianaire': info[2]} for info in ip_info]
    
    return jsonify(result)
	
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
