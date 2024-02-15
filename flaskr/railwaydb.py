import pymysql
from flask import current_app, g
from sqlalchemy.sql import text
from flaskr import config

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def setup_connection(app):
    if 'RAILWAY_MYSQL_URI' not in app.config:   
        app.config['SQLALCHEMY_DATABASE_URI'] = config.RAILWAY_MYSQL_URI
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        db.init_app(app)
    
    with app.app_context():
            try:
                # Perform a simple query to test the connection
                db.session.query(text('1')).from_statement(text('SELECT 1')).all()
                print("Database connection successful!")
            except Exception as e:
                print(f"Error establishing database connection: {e}")
    return db

def init_railway_app(app):

    app.teardown_appcontext(close_db)
    setup_connection(app)


def get_db():
    if 'db' not in g:
        g.db = db.session
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()