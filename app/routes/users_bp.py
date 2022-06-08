from .. import db
from flask import Blueprint, jsonify, request
from ..models import Project, Engineer

users = Blueprint('users', __name__)

#################### Users Routes ####################

# Get all users
@users.route('/', methods=['GET'])
def get_all_users():
    all_users = Engineer.query.all()
    return jsonify(engineers =[engineer.to_dict() for engineer in all_users])

# Create user
@users.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    user = Engineer(
        name = data['name'],
        #Todo encrypt password (ex.bcrypt)
        password = data['password']
    )
    db.session.add(user)
    db.session.commit()
    #Todo (return status code instead of string)
    return f'user {user.name} was created'

# Get single user
@users.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    user = Engineer.query.filter_by(id = user_id).first()
    return jsonify(engineer = user.to_dict())

# Update user
@users.route('/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = user = Engineer.query.filter_by(id = user_id).first()
    data = request.get_json()
    if user:
        if 'name' in data:
            user.name = data['name']
        if 'password' in data:
            # Todo password must be encrpyted when updated
            user.password = data['password'] 
        db.session.commit()
        return 'updated user'
    else:
        return 'Error'

# Delete user
@users.route('/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = Engineer.query.filter_by(id = user_id).first()
    db.session.delete(user)
    db.session.commit()
    #Todo (return status code instead of string)
    return f'user with id of {user_id} was deleted from database'


#################### Users/Projects Routes ####################

# Create a user project
@users.route('/<user_id>/projects', methods=['POST'])
def create_project(user_id):
    user = Engineer.query.filter_by(id = user_id).first()
    data = request.get_json()
    project = Project(
        name = data['name'],
        description = data['description'],
        is_complete = bool(data['is_complete'])
    )
    db.session.add(project)
    user.projects.append(project)
    db.session.commit()
    return f'Project {project.name} created for {user.name}'


# Get all user projects
@users.route('/<user_id>/projects', methods=['GET'])
def get_all_user_projects(user_id):
    user = Engineer.query.filter_by(id = user_id).first()
    user_projects = user.projects
    return jsonify(projects =[project.to_dict() for project in  user_projects])

# Get single user project
@users.route('/<user_id>/projects/<project_id>', methods=['GET'])
def get_user_project(user_id, project_id):
    user = Engineer.query.filter_by(id = user_id).first()
    single_project = None
    for project in user.projects:
        print(project.id)
        if project.id == int(project_id):
            single_project = project
            break
    if single_project:
        return jsonify(project = single_project.to_dict())
    else:
        return f'{user.name} does not have the project you are looking for'

# Update user project
@users.route('/<user_id>/projects/<project_id>', methods=['PUT'])
def update_user_project(user_id, project_id):
    user = Engineer.query.filter_by(id = user_id).first()
    project = Project.query.filter_by(id = project_id).first()
    data = request.get_json()
    if project in user.projects:
        if 'name' in data:
            project.name = data['name']
        if 'is_complete' in data:
            project.is_complete = data['is_complete']
        if 'description' in data:
            project.description = data['description']
    
        db.session.commit()
        return 'update_user_project'
    else:
        return 'Error'

# Delete user project
@users.route('/<user_id>/projects/<project_id>', methods=['DELETE'])
def delete_user_project(user_id, project_id):
    user = Engineer.query.filter_by(id = user_id).first()
    for project in user.projects[:]:
        if project.id == int(project_id):
            user.projects.remove(project)
            break
    db.session.commit()
    return f'Deleted project with id {project_id} from {user.name} list of projects'

#################### Users/Tasks Routes ####################

# Get all user tasks
@users.route('/<user_id>/tasks', methods=['GET'])
def get_all_user_tasks(user_id):
    user = Engineer.query.filter_by(id = user_id).first()
    user_tasks = user.tasks
    return jsonify(tasks =[task.to_dict() for task in  user_tasks])
