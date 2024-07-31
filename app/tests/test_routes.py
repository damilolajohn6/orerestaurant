import unittest
from app import create_app, db
from app.models import User, Menu
from werkzeug.security import generate_password_hash


class RoutesTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        # Create a test user and menu
        self.staff_user = User(username='staff', password=generate_password_hash('password', method='pbkdf2:sha256'),
                               role='staff')
        self.customer_user = User(username='customer',
                                  password=generate_password_hash('password', method='pbkdf2:sha256'), role='customer')
        self.menu_item = Menu(name='Pizza', description='Delicious pizza', price=9.99, category='food')
        db.session.add_all([self.staff_user, self.customer_user, self.menu_item])
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_place_order(self):
        # Login as customer
        login_response = self.client.post('/login', json={
            'username': 'customer',
            'password': 'password'
        })
        access_token = login_response.json['access_token']

        # Place order
        response = self.client.post('/orders', headers={
            'Authorization': f'Bearer {access_token}'
        }, json={
            'items': 'Pizza'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Order placed', response.json['msg'])


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
