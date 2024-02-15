import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .railwaydb import db, setup_connection
from flaskr import config
from sqlalchemy.sql import text


def create_app(test_config=None):
    # create and configure the app
    # create the app    
    db = SQLAlchemy()
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev', # secrets.token.hex(16) for prod
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
  
    #python way to import and inject stuff so that they can be executed via flask command as packages?
    # from . import sqllitedb
    # sqllitedb.init_app(app)
    
    # setup connection and link the sqlalchemy and flask app
    app.config['SQLALCHEMY_DATABASE_URI'] = config.RAILWAY_MYSQL_URI
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
    
    @app.route('/testconnection')
    def testdb():
        try:
            db.session.query(text('1')).from_statement(text('SELECT 1')).all()
            return '<h1>It works.</h1>'
        except Exception as e:
            # e holds description of the error
            error_text = "<p>The error:<br>" + str(e) + "</p>"
            hed = '<h1>Something is broken.</h1>'
            return hed + error_text

    return app


