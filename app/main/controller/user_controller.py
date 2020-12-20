from flask import request
from flask_restx import Resource, fields

from app.main.util.decorator import admin_token_required, token_required
from ..util.dto import UserDto
from ..service.user_service import get_all_users, get_a_user, save_farm, get_farm, save_robot, get_robot

api = UserDto.api

_user = {
    'username': fields.Raw,
    'public_id': fields.Raw,
    'email': fields.Raw,
    'phone': fields.Raw,
    'registered_robot_id': fields.Raw,
}
_farm = {
    'name':fields.Raw,
    'city':fields.Raw,
    'owner':fields.Raw,
    'public_id':fields.Raw,
    'user_id':fields.Raw
}
_robot = {
    'name' : fields.Raw,
    'model': fields.Raw,
    'public_id': fields.Raw,
    'user_id': fields.Raw,
    'pi_type': fields.Raw,
    'aurdino_type': fields.Raw,
    'motor_type': fields.Raw,
    'motor_driver_type': fields.Raw,
    'battey_info': fields.Raw,
    'public_url': fields.Raw,
    'public_pnumber':fields.Raw,
    'is_solar': fields.Raw,
    'is_led': fields.Raw,
}


@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @admin_token_required
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_users()


@api.route('/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @admin_token_required
    @api.marshal_with(_user)
    def get(self, public_id):
        """get a user given its identifier"""
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user


@api.route('/farm')
class UserFarm(Resource):
    """docstring for UserFarm"""
    @api.doc('get a farm details')
    @token_required
    @api.marshal_list_with(_farm,envelope='all_farm')
    def get(self):
        auth_header = request.headers.get('Authorization')
        return get_farm(auth_token=auth_header)

    @api.doc('save a farm details')
    @token_required
    def post(self):
        data = request.json
        auth_header = request.headers.get('Authorization')
        return save_farm(data=data,auth_token=auth_header)


@api.route('/robot')
class UserRobot(Resource):
    """docstring for UserFarm"""
    @api.doc('get a robot details')
    @token_required
    @api.marshal_with(_robot)
    def get(self):
        auth_header = request.headers.get('Authorization')
        return get_robot(auth_token=auth_header)

    @api.doc('save a robot details')
    @token_required
    def post(self):
        data = request.json
        auth_header = request.headers.get('Authorization')
        return save_robot(data=data,auth_token=auth_header)