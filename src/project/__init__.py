from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from project.configs import Config



db = SQLAlchemy()#variable base de datos
migrate = Migrate()#migrate para generar onjetos en la db
bcrypt = Bcrypt()

def register_blueprints(app):
    from project.endpoints import blueprint as usuarios

    app.register_blueprint(usuarios)


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)


    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    register_blueprints(app)

    return app
