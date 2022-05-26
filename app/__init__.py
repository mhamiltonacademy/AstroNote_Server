from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Astronote.sqlite"
    db.init_app(app)

    from .routes.users_bp import users
    from .routes.projects_bp import projects 

    app.register_blueprint(users, url_prefix='/users')
    app.register_blueprint(projects, url_prefix='/projects')

    from .models import Engineer, Project, Task
    create_database(app)
    return app


def create_database(app):
    db.create_all(app=app)
    print('Created Database!')