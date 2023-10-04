from flask import Flask, request, jsonify

app = Flask(__name__)

# Exemple de données sous forme de dictionnaire
data = {
    1: {'@ mac': 'ff:e4:3a:b3', '@ ip': '10.202.8.1'},
    2: {'@ mac': '', '@ ip': ''}
}

# Route pour obtenir tous les éléments
@app.route('/api/elements', methods=['GET'])
def obtenir_elements():
    return jsonify(data)

# Route pour obtenir un élément par son ID
@app.route('/api/elements/<int:element_id>', methods=['GET'])
def obtenir_element(element_id):
    element = data.get(element_id)
    if element:
        return jsonify(element)
    else:
        return jsonify({'message': 'Element non trouve'}), 404

# Route pour créer un nouvel élément
@app.route('/api/elements', methods=['POST'])
def creer_element():
    nouvel_element = request.get_json()
    if nouvel_element:
        nouvel_id = max(data.keys()) + 1
        data[nouvel_id] = nouvel_element
        return jsonify({'message': 'Element cree avec succes', 'id': nouvel_id}), 201
    else:
        return jsonify({'message': 'Donnees invalides'}), 400

# Route pour mettre à jour un élément par son ID
@app.route('/api/elements/<int:element_id>', methods=['PUT'])
def mettre_a_jour_element(element_id):
    element_existant = data.get(element_id)
    if element_existant:
        nouvelles_donnees = request.get_json()
        if nouvelles_donnees:
            element_existant.update(nouvelles_donnees)
            return jsonify({'message': 'Element mis a jour avec succes'}), 200
        else:
            return jsonify({'message': 'Donnees invalides'}), 400
    else:
        return jsonify({'message': 'Elément non trouve'}), 404

# Route pour supprimer un élément par son ID
@app.route('/api/elements/<int:element_id>', methods=['DELETE'])
def supprimer_element(element_id):
    element_existant = data.get(element_id)
    if element_existant:
        del data[element_id]
        return jsonify({'message': 'Element supprime avec succes'}), 200
    else:
        return jsonify({'message': 'Element non trouve'}), 404

if __name__ == '__main__':
    app.run(debug=True)
