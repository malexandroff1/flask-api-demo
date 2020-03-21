class User:
    def __init__(self, first_name=None, last_name=None, email=None, birthdate=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.birthdate = birthdate

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
