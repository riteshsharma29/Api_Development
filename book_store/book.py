from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps

"""
https://www.askpython.com/python-modules/flask/flask-rest-api
"""

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Book(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Integer())
    author = db.Column(db.String(80))

@app.route('/create', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book = Book(name=data['name'],price=data['price'],author=data['author'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message' : 'New Book Added!'}),201

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    output = []
    for book in books:
        book_data = {}
        book_data['id'] = book.id
        book_data['name'] = book.name
        book_data['price'] = book.price
        book_data['author'] = book.author
        output.append(book_data)
    return jsonify({'books': output})


@app.route('/books/<id>', methods=['GET'])
def get_book(id):
    book = Book.query.filter_by(id=id).first()

    if not book:
        return jsonify({'message' : 'No book found!'})

    book_data = {}
    book_data['name'] = book.name
    book_data['price'] = book.price
    book_data['author'] = book.author
    return jsonify({'books': book_data})


@app.route('/update/<id>', methods=['PUT'])
def update_book(id):
    book = Book.query.filter_by(id=id).first()

    if not book:
        return jsonify({'message' : 'No book found!'})

    data = request.get_json()
    if book:
        book.name = data['name']
        book.price = data['price']
        book.author = data['author']
    db.session.add(book)
    db.session.commit()
    return jsonify({'message' : 'book {} Updated'.format(id)})


@app.route('/delete/<id>', methods=['DELETE'])
def delete_todo(id):
    book_to_delete = Book.query.filter_by(id=id).first()

    if not book_to_delete:
        return jsonify({'message' : 'No book found!'})

    db.session.delete(book_to_delete)
    db.session.commit()

    return jsonify({'message' : 'book {} Deleted'.format(id)})



if __name__ == '__main__':
    app.run(debug=True)