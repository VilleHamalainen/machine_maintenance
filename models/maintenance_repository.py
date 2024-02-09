import os
from flask import Flask, request, current_app, g
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import click

db = SQLAlchemy()

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(current_app.config['DATABASE',], detect_types= sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row
    
    return g.db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

class Machine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    run_time = db.Column(db.Float)
    fuel_amount = db.Column(db.Float)



