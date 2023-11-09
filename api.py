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
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
