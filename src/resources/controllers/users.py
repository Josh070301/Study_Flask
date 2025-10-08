from flask_restful import Resource, reqparse
from flask import jsonify, request
from src.models.users import UserModel
from src import api
from configs.database import db

class Users(Resource):
    def get(self):
        users = UserModel.query.all()
        return {'data': [user.serialize_full() for user in users]}
    
    def post(self):
        data = request.get_json()
        name = data.get('name')
        if not name:
            return {'message': 'Name is required'}, 400
        
        email = data.get('email')
        if not email:
            return {'message': 'Email is required'}, 400
        
        password = data.get('password')
        if not password:
            return {'message': 'Password is required'}, 400
        

        new_user = UserModel(
            name=name,
            email=email,
            password=password,
        )
        db.session.add(new_user)
        db.session.commit()
        return {'message': 'User created', 'user': new_user.serialize_full()}, 201
    
    # PUT with Optional columns
    def put(self):
        data = request.get_json()
        user_id = data.get('id')
        name = data.get('name')
        if not user_id:
            return {'message': 'ID is required'}, 400
        
        user = UserModel.query.get(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        
        if 'name' in data:
            user.name = data['name']
        if 'email' in data:
            user.email = data['email']
        if 'password' in data:
            user.password = data['password']
        if 'isArchived' in data:
            user.isArchived = data['isArchived']

        db.session.commit()
        return {'message': 'User updated', 'user': user.serialize_full()}, 200

api.add_resource(Users, '/users', strict_slashes=False)