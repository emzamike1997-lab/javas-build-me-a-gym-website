from flask import Blueprint, request, jsonify
from services import UserService, GymService, MembershipService
from models import User, Gym, Membership
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity

main = Blueprint('main', __name__)

@main.route('/register', methods=['POST'])
def register():
    """Register a new user"""
    username = request.json.get('username')
    email = request.json.get('email')
    password = request.json.get('password')
    user = UserService.create_user(username, email, password)
    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token)

@main.route('/login', methods=['POST'])
def login():
    """Login a user"""
    email = request.json.get('email')
    password = request.json.get('password')
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token)
    return jsonify(error='Invalid email or password'), 401

@main.route('/gyms', methods=['GET'])
@jwt_required
def get_gyms():
    """Get all gyms"""
    gyms = Gym.query.all()
    return jsonify([gym.name for gym in gyms])

@main.route('/gyms', methods=['POST'])
@jwt_required
def create_gym():
    """Create a new gym"""
    name = request.json.get('name')
    address = request.json.get('address')
    gym = GymService.create_gym(name, address)
    return jsonify(gym.name)

@main.route('/memberships', methods=['POST'])
@jwt_required
def create_membership():
    """Create a new membership"""
    user_id = get_jwt_identity()
    gym_id = request.json.get('gym_id')
    start_date = request.json.get('start_date')
    end_date = request.json.get('end_date')
    membership = MembershipService.create_membership(user_id, gym_id, start_date, end_date)
    return jsonify(membership.id)
```

###