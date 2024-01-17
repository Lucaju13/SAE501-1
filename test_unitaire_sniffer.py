import unittest
import guisniff  # Assurez-vous que le nom du fichier est correct

class TestGuiSniffApp(unittest.TestCase):

    def setUp(self):
        # Créer une instance de l'application pour les tests
        self.app = guisniff.App()

    def test_setup_database(self):
        # Vérifier que la base de données et le curseur sont initialisés
        self.assertIsNotNone(self.app.conn)
        self.assertIsNotNone(self.app.cursor)

    def test_start_sniffing_threaded(self):
        # Vérifier que le thread de sniffing est lancé correctement
        self.app.start_sniffing_threaded()
        self.assertTrue(self.app.sniffing_thread.is_alive())

    def test_stop_sniffing(self):
        # Vérifier que le sniffing s'arrête correctement
        self.app.start_sniffing_threaded()
        self.app.stop_sniffing()
        self.assertFalse(self.app.sniffing_active)

    def test_detecter_alertes(self):
        # Vérifier la fonction de détection d'alertes
        # Vous devrez peut-être adapter cela en fonction de la structure réelle de votre base de données
        # Assurez-vous d'avoir une trame d'exemple dans la base de données pour les tests
        self.app.setup_database()  # S'assurer que la base de données est initialisée
        self.app.detecter_alertes()
        self.assertNotEqual(self.app.box_affichage_erreurs.get("1.0", "end"), "")


    def tearDown(self):
        # Fermer la connexion à la base de données après les tests
        self.app.conn.close()

if __name__ == '__main__':
    unittest.main()
