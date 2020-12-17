from flask import request
from flask_restx import Resource

from app.main.service.auth_service import Auth
from app.main.util.dto import AuthDto, UserDto

api = AuthDto.api
user_auth = AuthDto.user_auth
_user = UserDto.user


@api.route('/login')
class LoginAPI(Resource):
    """
        User Login Resource
    """
    @api.doc('user login')
    @api.expect(user_auth, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        return Auth.login_user(data=post_data)


@api.route('/logout')
class LogoutAPI(Resource):
    """
        Logout Resource
    """
    @api.doc('logout a user')
    def get(self):
        # get auth token
        auth_header = request.headers.get('Authorization')
        return Auth.logout_user(auth_token=auth_header)


@api.route('/signup')
class SignupAPI(Resource):
    """
        Signup Resource
    """
    @api.doc('Signup a user')
    @api.expect(_user, validate=True)
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    def post(self):
        """Creates a new User """
        data = request.json
        is_admin = True if request.headers.get('admin_secret_key') == 'maibhiadmin' else False
        print(is_admin)
        return Auth.signup_user(data=data, is_admin=is_admin)
