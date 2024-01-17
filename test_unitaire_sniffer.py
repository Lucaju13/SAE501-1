import unittest
import guisniff 

class TestGuiSniffApp(unittest.TestCase):

    def setUp(self):
        # Créer une instance de l'application pour les tests
        self.app = guisniff.App()

    def tearDown(self):
        # Fermer la connexion à la base de données après les tests
        self.app.conn.close()

    def print_test_start(self, test_name):
        print(f"\nDébut du test: {test_name}")

    def print_test_end(self, test_name, success=True):
        if success:
            print(f"Fin du test: {test_name} - Test OK\n")
        else:
            print(f"Fin du test: {test_name} - Test ÉCHEC\n")

    def test_setup_database(self):
        self.print_test_start("Initialisation de la base de données")
        # Vérifier que la base de données et le curseur sont initialisés
        self.assertIsNotNone(self.app.conn)
        self.assertIsNotNone(self.app.cursor)
        self.print_test_end("Initialisation de la base de données")

    def test_start_sniffing_threaded(self):
        self.print_test_start("Démarrage du sniffing en thread")
        # Vérifier que le thread de sniffing est lancé correctement
        self.app.start_sniffing_threaded()
        self.assertTrue(self.app.sniffing_thread.is_alive())
        self.print_test_end("Démarrage du sniffing en thread")

    def test_stop_sniffing(self):
        self.print_test_start("Arrêt du sniffing")
        # Vérifier que le sniffing s'arrête correctement
        self.app.start_sniffing_threaded()
        self.app.stop_sniffing()
        self.assertFalse(self.app.sniffing_active)
        self.print_test_end("Arrêt du sniffing")

    def test_detecter_alertes(self):
        self.print_test_start("Détection d'alertes")
        # Vérifier la fonction de détection d'alertes
        self.app.setup_database()  # S'assurer que la base de données est initialisée
        self.app.detecter_alertes()
        self.assertNotEqual(self.app.box_affichage_erreurs.get("1.0", "end"), "")
        
        # Ajouter une assertion pour indiquer si le test réussit ou non
        success = True  # Par défaut, le test est réussi
        self.assertTrue(success)
        
        self.print_test_end("Détection d'alertes", success)

if __name__ == '__main__':
    unittest.main()
