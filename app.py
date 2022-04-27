from flask import Flask, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Astronote'
# db = SQLAlchemy(app)

#################### Users Routes ####################
@app.route('/users', methods = ['GET'])
def get_all_users():
    return 'Retrieves ALL users'

@app.route('/users/<user_id>', methods = ['POST'])
def create_user(user_id):
    return 'create user'

@app.route('/users/<user_id>', methods = ['GET'])
def get_user(user_id):
    return f'get {user_id}'

@app.route('/users/<user_id>', methods = ['PUT'])
def update_user(user_id):
    return 'update_user'

@app.route('/users/<user_id>', methods = ['DELETE'])
def delete_user(user_id):
    return 'delete_user'

#################### Users/Projects Routes ####################
@app.route('/users/<user_id>/projects', methods = ['POST'])
def create_project(user_id):
    return 'create a user\'s project'

@app.route('/users/<user_id>/projects', methods = ['GET'])
def get_all_user_projects(user_id):
    return 'Retrieves all of a users projects'

@app.route('/users/<user_id>/projects/<project_id>', methods = ['GET'])
def get_user_project(user_id, project_id):
    return 'get_user_project'

@app.route('/users/<user_id>/projects/<project_id>', methods = ['PUT'])
def update_user_project(user_id, project_id):
    return 'update_user_project'

@app.route('/users/<user_id>/projects/<project_id>', methods = ['DELETE'])
def delete_user_project(user_id, project_id):
    return 'delete_user_project'

#################### Users/Tasks Routes ####################
@app.route('/users/<user_id>/tasks', methods = ['GET'])
def get_all_user_tasks(user_id):
    return 'Retrieves ALL of a users tasks'

#################### Projects Routes ####################
@app.route('/projects/<project_id>/users', methods = ['GET'])
def get_users_in_project(project_id):
    return 'Retrieves all the users working on a project'

#################### Projects/Tasks Routes ####################
@app.route('/projects/<project_id>/tasks', methods = ['POST'])
def create_tasks_in_project(project_id):
    return 'Creates a task for a project'

@app.route('/projects/<project_id>/tasks/<task_id>', methods = ['PUT'])
def update_project_tasks(project_id, task_id):
    return 'Updates a projects tasks'

@app.route('/projects/<project_id>/tasks/<task_id>', methods = ['DELETE'])
def delete_project_tasks(project_id, task_id):
    return 'Deletes tasks'

if __name__ == "__main__":
    app.run(debug=True)


