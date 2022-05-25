from flask import Flask, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from routes.users_bp import users
from routes.projects_bp import projects


app = Flask(__name__)
app.register_blueprint(users, url_prefix='/users')
app.register_blueprint(projects, url_prefix='/projects')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/Astronote'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Astronote.sqlite"
db = SQLAlchemy(app)






@app.route('/', methods=['GET'])
def get_all_users():
    return 'HOMEPAGE'


if __name__ == "__main__":
    app.run(debug=False)
