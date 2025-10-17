from flask import request
from flask_restful import Resource
from src import api

class add(Resource):
    def post(self):
        first_number = request.args.get('firstNumber', None)
        second_number = request.args.get('secondNumber', None)

        if first_number is None or second_number is None:
            return {'message': 'Both firstNumber and secondNumber are required'}, 400
        # Implement your logic to add a new resource

        return {'message': 'Resource added', 'sum': int(first_number) + int(second_number)}, 201
    
class substract(Resource):
    def post(self):
        first_number = request.args.get('firstNumber', None)
        second_number = request.args.get('secondNumber', None)

        if first_number is None or second_number is None:
            return {'message': 'Both firstNumber and secondNumber are required'}, 400
        # Implement your logic to subtract a resource

        return {'message': 'Resource subtracted', 'difference': int(first_number) - int(second_number)}, 201
    
class multiply(Resource):
    def post(self):
        first_number = request.args.get('firstNumber', None)
        second_number = request.args.get('secondNumber', None)

        if first_number is None or second_number is None:
            return {'message': 'Both firstNumber and secondNumber are required'}, 400
        # Implement your logic to multiply a resource

        return {'message': 'Resource multiplied', 'product': int(first_number) * int(second_number)}, 201
    
class divide(Resource):
    def post(self):
        first_number = request.args.get('firstNumber', None)
        second_number = request.args.get('secondNumber', None)

        if first_number is None or second_number is None:
            return {'message': 'Both firstNumber and secondNumber are required'}, 400
        if int(second_number) == 0:
            return {'message': 'Division by zero is not allowed'}, 400
        # Implement your logic to divide a resource

        return {'message': 'Resource divided', 'quotient': int(first_number) / int(second_number)}, 201
    
api.add_resource(add, '/add', strict_slashes=False)
api.add_resource(substract, '/substract', strict_slashes=False)
api.add_resource(multiply, '/multiply', strict_slashes=False)
api.add_resource(divide, '/divide', strict_slashes=False)

students = [
    {'id': 1, 'name': 'John Doe', 'nickname': 'Johnny'},
    {'id': 2, 'name': 'Jane Smith', 'nickname': 'Janey'},
    {'id': 3, 'name': 'Alice Johnson', 'nickname': 'Ali'}
]

class student(Resource):
    
    def get(self):
        return {'data': students}, 200
    
    def post(self):
        data = request.get_json()
        print("POSITNG DATA: ", data)
        name = data.get('name')
        nickname = data.get('nickname')
        if not name:
            return {'message': 'Name is required'}, 400
        
        if not nickname:
            return {'message': 'Nickname is required'}, 400
        
        new_id = max(student['id'] for student in students) + 1 if students else 1
        new_student = {'id': new_id, 'name': name, 'nickname': nickname }
        students.append(new_student)
        return {'message': 'Student added', 'student': new_student}, 201
    
    def put(self, id):
        data = request.get_json()
        name = data.get('name', None)
        nickname = data.get('nickname', None)

        print(id, name, nickname)

        if not id:
            return {'message': 'ID is required'}, 400

        for student in students:

            if student['id'] == int(id):
                if name is not None:
                    student['name'] = name

                if nickname is not None:
                    student['nickname'] = nickname

                return {'message': 'Student updated', 'student': student}, 200


        return {'message': 'Student not found'}, 404
    
    def delete(self, id):
        if not id:
            return {'message': 'ID is required'}, 400

        for student in students:
            if student['id'] == int(id):
                students.remove(student)
                return {'message': 'Student deleted'}, 200

        return {'message': 'Student not found'}, 404

api.add_resource(student, '/students', '/students/<id>', strict_slashes=False)

