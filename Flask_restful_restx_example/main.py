from flask import Flask,  request, jsonify, make_response
# import flask_restful
# from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api, Resource, fields


"""
reference Blog : https://www.youtube.com/watch?v=G3lPb6mlqTA&t=702s
https://stackoverflow.com/questions/30779584/flask-restful-passing-parameters-to-get-request
"""

# create an instance of flask
app = Flask(__name__)
# creating an API object
api = Api(app)
# create database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#sqlalchemy mapper
db = SQLAlchemy(app)

# add a class
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(80), nullable=False)
    salary = db.Column(db.Float)

    def __repr__(self):
        return f"{self.firstname} - {self.lastname} - {self.gender} - {self.salary}"

################   GET ##############################

# For GET request to http://localhost:5000/
class GetEmployee(Resource):
    def get(self):
        employees = Employee.query.all()
        emp_list = []
        for emp in employees:
            emp_data = {'Id': emp.id, 'FirstName': emp.firstname, 'LastName': emp.lastname, 'Gender': emp.gender,
                        'Salary': emp.salary}
            emp_list.append(emp_data)
        return {"Employees": emp_list}, 200

class GetEmployeeById(Resource):
    def get(self,ID):
        employees = Employee.query.all()
        emp_data = {}
        for emp in employees:
            if emp.id == ID:
                emp_data = {'Id': emp.id, 'FirstName': emp.firstname, 'LastName': emp.lastname, 'Gender': emp.gender,
                            'Salary': emp.salary}
                break
        return(emp_data), 200

class GetEmployeeByName(Resource):
    def get(self,Name):
        employees = Employee.query.all()
        emp_data = {}
        for emp in employees:
            if emp.firstname == Name:
                emp_data = {'Id': emp.id, 'FirstName': emp.firstname, 'LastName': emp.lastname, 'Gender': emp.gender,
                            'Salary': emp.salary}
                break
        return(emp_data), 200


class GetEmployeeByIDAndName(Resource):
    def get(self,ID,Name):
        employees = Employee.query.all()
        emp_data = {}
        for emp in employees:
            if emp.firstname == Name and emp.id == ID:
                emp_data = {'Id': emp.id, 'FirstName': emp.firstname, 'LastName': emp.lastname, 'Gender': emp.gender,
                            'Salary': emp.salary}
                break
        return(emp_data), 200

api.add_resource(GetEmployee, '/All')
api.add_resource(GetEmployeeById, '/<int:ID>')
api.add_resource(GetEmployeeByName, '/<string:Name>')
api.add_resource(GetEmployeeByIDAndName, '/<int:ID>&<string:Name>')

################  POST ##############################

class AddEmployee(Resource):
    def post(self):
        if request.is_json:
            emp = Employee(firstname=request.json['FirstName'], lastname=request.json['LastName'],
                       gender=request.json['Gender'], salary=request.json['Salary'])
            db.session.add(emp)
            db.session.commit()
            # return a json response
            return make_response(jsonify({'Id': emp.id, 'First Name': emp.firstname, 'Last Name': emp.lastname,
                                          'Gender': emp.gender, 'Salary': emp.salary}), 201)
        else:
            return {'error': 'Request must be JSON'}, 400

# For Post request to http://localhost:5000/employee
class AddEmployeeParam(Resource):
    def post(self,FirstName,LastName,Gender,Salary):
        emp = Employee(firstname=FirstName, lastname=LastName,
                       gender=Gender, salary=Salary)
        db.session.add(emp)
        db.session.commit()
        # return a json response
        return make_response(jsonify({'Id': emp.id, 'First Name': emp.firstname, 'Last Name': emp.lastname,
                                      'Gender': emp.gender, 'Salary': emp.salary}), 201)


api.add_resource(AddEmployee, '/add')
api.add_resource(AddEmployeeParam, '/addParam/<string:FirstName>&<string:LastName>&<string:Gender>&<float:Salary>')


################  PUT ##############################

# For put request to http://localhost:5000/update/?
class UpdateEmployee(Resource):
    def put(self, id):
        if request.is_json:
            emp = Employee.query.get(id)
            if emp is None:
                return {'error': 'not found'}, 404
            else:
                emp.firstname = request.json['FirstName']
                emp.lastname = request.json['LastName']
                emp.gender = request.json['Gender']
                emp.salary = request.json['Salary']
                db.session.commit()
                return 'Updated', 200
        else:
            return {'error': 'Request must be JSON'}, 400

api.add_resource(UpdateEmployee, '/update/<int:id>')

################ DELETE ##############################

# For delete request to http://localhost:5000/delete/?
class DeleteEmployee(Resource):
    def delete(self, id):
        emp = Employee.query.get(id)
        if emp is None:
            return {'error': 'not found'}, 404
        db.session.delete(emp)
        db.session.commit()
        return f'{id} is deleted', 200

api.add_resource(DeleteEmployee, '/delete/<int:id>')

#
if __name__ == '__main__':
    app.run(debug=True)
