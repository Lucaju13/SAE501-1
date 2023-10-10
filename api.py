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

# Route pour créer un nouvel élément
@app.route('/api/elements', methods=['POST'])
def creer_element():
    nouvel_element = request.get_json()
    if nouvel_element:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO data (mac, ip) VALUES (?, ?)",
                       (nouvel_element.get('@ mac'), nouvel_element.get('@ ip')))
        conn.commit()
        nouvel_id = cursor.lastrowid
        conn.close()
        return jsonify({'message': 'Element cree avec succes', 'id': nouvel_id}), 201
    else:
        return jsonify({'message': 'Donnees invalides'}), 400

# Route pour mettre à jour un élément par son ID
@app.route('/api/elements/<int:element_id>', methods=['PUT'])
def mettre_a_jour_element(element_id):
    element_existant = request.get_json()
    if element_existant:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE data SET mac=?, ip=? WHERE id=?",
                       (element_existant.get('@ mac'), element_existant.get('@ ip'), element_id))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Element mis a jour avec succes'}), 200
    else:
        return jsonify({'message': 'Donnees invalides'}), 400

# Route pour supprimer un élément par son ID
@app.route('/api/elements/<int:element_id>', methods=['DELETE'])
def supprimer_element(element_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM data WHERE id=?", (element_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Element supprime avec succes'}), 200

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
