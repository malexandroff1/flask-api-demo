from app.models import User

class UserRepository:
    @staticmethod
    def create(payload):
        return User.from_dict(payload)
