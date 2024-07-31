import unittest
from app import create_app, db
from app.models import User
from werkzeug.security import generate_password_hash


class AuthTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_register(self):
        response = self.client.post('/register', json={
            'username': 'testuser',
            'password': 'testpassword',
            'role': 'customer'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('User registered', response.json['msg'])

    def test_login(self):
        # Register user
        self.client.post('/register', json={
            'username': 'testuser',
            'password': 'testpassword',
            'role': 'customer'
        })
        # Login user
        response = self.client.post('/login', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', response.json)


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
