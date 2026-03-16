from app import db
from models import User, Gym, Membership
from datetime import datetime

class UserService:
    """User service"""
    @staticmethod
    def create_user(username, email, password):
        """Create a new user"""
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_user(user_id):
        """Get a user by ID"""
        return User.query.get(user_id)

class GymService:
    """Gym service"""
    @staticmethod
    def create_gym(name, address):
        """Create a new gym"""
        gym = Gym(name=name, address=address)
        db.session.add(gym)
        db.session.commit()
        return gym

    @staticmethod
    def get_gym(gym_id):
        """Get a gym by ID"""
        return Gym.query.get(gym_id)

class MembershipService:
    """Membership service"""
    @staticmethod
    def create_membership(user_id, gym_id, start_date, end_date):
        """Create a new membership"""
        membership = Membership(user_id=user_id, gym_id=gym_id, start_date=start_date, end_date=end_date)
        db.session.add(membership)
        db.session.commit()
        return membership

    @staticmethod
    def get_membership(membership_id):
        """Get a membership by ID"""
        return Membership.query.get(membership_id)
```

###