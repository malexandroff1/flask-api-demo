from app.schemas import UserSchema
from app.repositories import UserRepository

class UserService:
    @staticmethod
    def create(payload):
        user_schema = UserSchema()
        user_dict = user_schema.load(payload)
        user = UserRepository.create(user_dict)
        return user_schema.dump(user)
