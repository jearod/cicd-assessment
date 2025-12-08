import unittest
import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        # Configurar el cliente de pruebas
        self.app = app.app.test_client()
        self.app.testing = True

    def test_home(self):
        # Verificar que la ruta '/' devuelve 200 y el mensaje correcto
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello DevOps World', response.data)

    def test_health(self):
        # Verificar endpoint de salud
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'healthy', response.data)

if __name__ == "__main__":
    unittest.main()