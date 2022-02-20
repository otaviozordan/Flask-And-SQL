from lib2to3.pgen2 import token
from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/teste'
db = SQLAlchemy(app)

class Data_API(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    token = db.Column(db.String(50))
    key = db.Column(db.String(100))

    def to_json(self):
        return {"id": self.id, "token": self.token, "key": self.key}

db.create_all()