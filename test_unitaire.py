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

    def print_test_start(self, test_name):
        print(f"===== Début du test : {test_name} =====")

    def print_test_end(self, test_name):
        print(f"===== Fin du test : {test_name} =====\n")

    def test_run_script_route(self):
        self.print_test_start("test_run_script_route")
        # Testez la route qui exécute le script
        response = requests.get('http://localhost:5000/api/run_script')
        print(f"Réponse de la requête : {response.text}")
        self.assertEqual(response.status_code, 200)
        self.assertIn('Script exécuté avec succès', response.json()['message'])
        self.print_test_end("test_run_script_route")

    def test_obtenir_elements_route(self):
        self.print_test_start("test_obtenir_elements_route")
        # Testez la route pour obtenir tous les éléments
        response = requests.get('http://localhost:5000/api/elements')
        print(f"Réponse de la requête : {response.text}")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertGreater(len(response.json()), 0)
        self.print_test_end("test_obtenir_elements_route")

    def test_obtenir_element_par_id_route(self):
        self.print_test_start("test_obtenir_element_par_id_route")
        # Testez la route pour obtenir un élément par son ID
        response = requests.get('http://localhost:5000/api/elements/6')
        print(f"Réponse de la requête : {response.text}")
        self.assertEqual(response.status_code, 200)
        self.assertIn('ID', response.json())
        self.print_test_end("test_obtenir_element_par_id_route")

    def test_obtenir_ip_destinataire_route(self):
        self.print_test_start("test_obtenir_ip_destinataire_route")
        # Testez la route pour obtenir toutes les adresses IP destinataires
        response = requests.get('http://localhost:5000/api/dst_ip')
        print(f"Réponse de la requête : {response.text}")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertGreater(len(response.json()), 0)
        self.print_test_end("test_obtenir_ip_destinataire_route")

    
    def test_obtenir_info_ip_dst_route(self):
        self.print_test_start("test_obtenir_info_ip_dst_route")
        # Testez la route pour obtenir des informations sur une adresse IP destinataire spécifique
        response = requests.get('http://localhost:5000/api/dst_ip/10.202.255.254')
        print(f"Réponse de la requête : {response.text}")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.print_test_end("test_obtenir_info_ip_dst_route")

    def test_obtenir_ip_source_route(self):
        self.print_test_start("test_obtenir_ip_source_route")
        # Testez la route pour obtenir toutes les adresses IP source
        response = requests.get('http://localhost:5000/api/src_ip')
        print(f"Réponse de la requête : {response.text}")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertGreater(len(response.json()), 0)
        self.print_test_end("test_obtenir_ip_source_route")

    def test_obtenir_info_ip_src_route(self):
        self.print_test_start("test_obtenir_info_ip_src_route")
        # Testez la route pour obtenir des informations sur une adresse IP source spécifique
        response = requests.get('http://localhost:5000/api/src_ip/10.202.255.254')
        print(f"Réponse de la requête : {response.text}")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.print_test_end("test_obtenir_info_ip_src_route")

    def test_obtenir_capture_time_route(self):
        self.print_test_start("test_obtenir_capture_time_route")
        # Testez la route pour obtenir tous les temps de capture
        response = requests.get('http://localhost:5000/api/capture_time')
        print(f"Réponse de la requête : {response.text}")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertGreater(len(response.json()), 0)
        self.print_test_end("test_obtenir_capture_time_route")

    def test_obtenir_type_trame_route(self):
        self.print_test_start("test_obtenir_type_trame_route")
        # Testez la route pour obtenir tous les types de trame
        response = requests.get('http://localhost:5000/api/type_trame')
        print(f"Réponse de la requête : {response.text}")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertGreater(len(response.json()), 0)
        self.print_test_end("test_obtenir_type_trame_route")

    def test_obtenir_nombre_trame_par_ip_src_route(self):
        self.print_test_start("test_obtenir_nombre_trame_par_ip_src_route")
        # Testez la route pour obtenir le nombre de trames par adresse IP source
        response = requests.get('http://localhost:5000/api/nombre_trame_par_ip_src')
        print(f"Réponse de la requête : {response.text}")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertGreater(len(response.json()), 0)
        self.print_test_end("test_obtenir_nombre_trame_par_ip_src_route")

    
    def test_obtenir_nombre_trame_par_ip_dst_route(self):
        self.print_test_start("test_obtenir_nombre_trame_par_ip_dst_route")
        # Testez la route pour obtenir le nombre de trames par adresse IP destinataire
        response = requests.get('http://localhost:5000/api/nombre_trame_par_ip_dst')
        print(f"Réponse de la requête : {response.text}")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertGreater(len(response.json()), 0)
        self.print_test_end("test_obtenir_nombre_trame_par_ip_dst_route")


     def test_obtenir_info_ip_dst_route(self):
        self.print_test_start("test_obtenir_info_ip_dst_route")
        # Testez la route pour obtenir des informations sur une adresse IP destinataire spécifique
        response = requests.get('http://localhost:5000/api/dst_ip/10.202.255.254')
        print(f"Réponse de la requête : {response.text}")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.print_test_end("test_obtenir_info_ip_dst_route")

     def test_obtenir_info_ip_src_route(self):
        self.print_test_start("test_obtenir_info_ip_src_route")
        # Testez la route pour obtenir des informations sur une adresse IP source spécifique
        response = requests.get('http://localhost:5000/api/src_ip/10.202.255.254')
        print(f"Réponse de la requête : {response.text}")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.print_test_end("test_obtenir_info_ip_src_route")


if __name__ == '__main__':
    unittest.main()
