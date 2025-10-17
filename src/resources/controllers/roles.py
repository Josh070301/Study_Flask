from flask_restful import Resource, reqparse
from flask import jsonify, request
from src.models.roles import RolesModel
from src import api
from configs.database import db

class Roles(Resource):
    def get(self):
        roles = RolesModel.query.all()
        return {'data': [role.serialize_full() for role in roles]}

api.add_resource(Roles, '/roles', strict_slashes=False)