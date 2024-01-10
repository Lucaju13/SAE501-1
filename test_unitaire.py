import unittest
import requests
import subprocess
import time

class TestFlaskApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Lancez l'application Flask dans un processus séparé pour les tests
        cls.flask_process = subprocess.Popen(['python3', 'api.py'])
        # Attendez un certain temps pour permettre au serveur Flask de démarrer
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        # Arrêtez le processus Flask après les tests
        cls.flask_process.terminate()
        cls.flask_process.wait()

    @classmethod
    def test2(cls):
        print("Début du test 2")
        response = requests.get('http://localhost:5000/api/elements')
        print(f"Réponse de la requête : {response.text}")
        print("Fin du test 2")

    def test_run_script_route(self):
        response = requests.get('http://localhost:5000/api/run_script')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Script exécuté avec succès', response.json()['message'])

    def test_obtenir_elements_route(self):
        response = requests.get('http://localhost:5000/api/elements')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertGreater(len(response.json()), 0)

    def test_obtenir_element_par_id_route(self):
        response = requests.get('http://localhost:5000/api/elements/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('id', response.json())

# Ajoutez d'autres tests pour les autres routes de votre application

if __name__ == '__main__':
    unittest.main()
