from app.models import User


class UserRepository:
    @staticmethod
    def create(payload):
        return User(**payload)
