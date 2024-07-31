from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import db, User, Menu, Order

bp = Blueprint('routes', __name__)

def is_staff():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    return user.role == 'staff'

@bp.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    if not is_staff():
        return jsonify({"msg": "You do not have the permission to access this resource"}), 403
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@bp.route('/users/<int:id>', methods=['GET'])
@jwt_required()
def get_user(id):
    if not is_staff():
        return jsonify({"msg": "You do not have the permission to access this resource"}), 403
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict())

@bp.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict())

@bp.route('/orders', methods=['POST'])
@jwt_required()
def place_order():
    user_id = get_jwt_identity()
    data = request.get_json()
    new_order = Order(customer_id=user_id, items=data['items'])
    db.session.add(new_order)
    db.session.commit()
    return jsonify({"msg": "Order placed"}), 201

@bp.route('/orders', methods=['GET'])
@jwt_required()
def get_orders():
    if not is_staff():
        return jsonify({"msg": "You do not have the permission to access this resource"}), 403
    orders = Order.query.all()
    return jsonify([order.to_dict() for order in orders])

@bp.route('/orders/<int:id>', methods=['GET'])
@jwt_required()
def get_order(id):
    order = Order.query.get_or_404(id)
    if not is_staff() and order.customer_id != get_jwt_identity():
        return jsonify({"msg": "You do not have the permission to access this resource"}), 403
    return jsonify(order.to_dict())
