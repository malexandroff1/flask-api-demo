from flask import request
from marshmallow.exceptions import ValidationError
from app import app
from app.services import UserService

@app.route('/users/', methods=['GET', 'POST'])
def user_view():
    def get():
        return {'method': 'get'}, 200

    def post():
        error = None
        user = None
        code = 201
        try:
            payload = request.get_json()
            user = UserService.create(payload)
        except ValidationError as exception:
            code = 400
            error = exception.messages
        return {'data': user, 'error': error}, code

    handlers = {
        'GET': get,
        'POST': post
    }

    return handlers[request.method.upper()]()
