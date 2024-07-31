from . import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # 'staff' or 'customer'

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200))
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50))  # 'food' or 'drink'
    discounted = db.Column(db.Boolean, default=False)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    items = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(50), default='placed')


def user_to_dict(user):
    return {
        "id": user.id,
        "username": user.username,
        "role": user.role
    }


def menu_to_dict(menu):
    return {
        "id": menu.id,
        "name": menu.name,
        "description": menu.description,
        "price": menu.price,
        "category": menu.category,
        "discounted": menu.discounted
    }


def order_to_dict(order):
    return {
        "id": order.id,
        "customer_id": order.customer_id,
        "items": order.items,
        "status": order.status
    }


User.to_dict = user_to_dict
Menu.to_dict = menu_to_dict
Order.to_dict = order_to_dict
