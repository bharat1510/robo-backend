import uuid
import datetime

from flask import jsonify
from app.main import db
from app.main.model.user import User
from app.main.model.farm import Farm
from app.main.model.robot import Robot

def get_all_users():
	return User.query.all()


def get_a_user(public_id):
	return User.query.filter_by(public_id=public_id).first()


def save_changes(data):
	db.session.add(data)
	db.session.commit()


def save_farm(data, auth_token):
	if auth_token:
		resp = User.decode_auth_token(auth_token)
		if not isinstance(resp, str):
			user = User.query.filter_by(id=resp).first()
			new_farm = Farm(
				public_id=str(uuid.uuid4()),
				user_id=user.public_id,
				name=data['name'],
				city=data['city'],
				owner=data['owner'],
				registered_on=datetime.datetime.utcnow()
			)
			save_changes(new_farm)
			response_object = {
				'status': 'success',
				'message': 'Successfully saved.',
			}
			return response_object, 201
		else:
			response_object = {
				'status': 'fail',
				'message': resp
			}
			return response_object, 401
	else:
		response_object = {
			'status': 'fail',
			'message': 'Provide a valid auth token.'
		}
		return response_object, 403


def get_farm(auth_token):
	if auth_token:
		resp = User.decode_auth_token(auth_token)
		if not isinstance(resp, str):
			user_publicid = User.query.filter_by(id=resp).first().public_id
			return Farm.query.filter_by(user_id=user_publicid).first()
		else:
			response_object = {
				'status': 'fail',
				'message': resp
			}
			return response_object, 401
	else:
		response_object = {
			'status': 'fail',
			'message': 'Provide a valid auth token.'
		}
		return response_object, 403


def save_robot(data, auth_token):
	if auth_token:
		resp = User.decode_auth_token(auth_token)
		if not isinstance(resp, str):
			user = User.query.filter_by(id=resp).first()
			new_robot = Robot(
				public_id=str(uuid.uuid4()),
				user_id=user.public_id,
				name=data['name'],
				model=data['model'],
				pi_type=data['pi_type'],
				aurdino_type=data['aurdino_type'],
				motor_type=data['motor_type'],
				motor_driver_type=data['motor_driver_type'],
				battey_info=data['battey_info'],
				public_url=data['public_url'],
				public_pnumber=data['public_pnumber'],
				is_solar = data['is_solar'],
    			is_led = data['is_led'],
				registered_on=datetime.datetime.utcnow()
			)
			save_changes(new_robot)
			response_object = {
				'status': 'success',
				'message': 'Successfully saved.',
			}
			return response_object, 201
		else:
			response_object = {
				'status': 'fail',
				'message': resp
			}
			return response_object, 401
	else:
		response_object = {
			'status': 'fail',
			'message': 'Provide a valid auth token.'
		}
		return response_object, 403


def get_robot(auth_token):
	if auth_token:
		resp = User.decode_auth_token(auth_token)
		if not isinstance(resp, str):
			user_publicid = User.query.filter_by(id=resp).first().public_id
			return Robot.query.filter_by(user_id=user_publicid).first()
		else:
			response_object = {
				'status': 'fail',
				'message': resp
			}
			return response_object, 401
	else:
		response_object = {
			'status': 'fail',
			'message': 'Provide a valid auth token.'
		}
		return response_object, 403