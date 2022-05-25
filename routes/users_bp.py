from flask import Blueprint
# from models import Project, Task, Engineer

users = Blueprint('users', __name__)

#################### Users Routes ####################


@users.route('/', methods=['GET'])
def get_all_users():
    return 'Retrieves ALL users'


@users.route('/<user_id>', methods=['POST'])
def create_user(user_id):
    return 'create user'


@users.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    return f'get {user_id}'


@users.route('/<user_id>', methods=['PUT'])
def update_user(user_id):
    return 'update_user'


@users.route('/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    return 'delete_user'


#################### Users/Projects Routes ####################


@users.route('/<user_id>/projects', methods=['POST'])
def create_project(user_id):
    return 'create a user\'s project'


@users.route('/<user_id>/projects', methods=['GET'])
def get_all_user_projects(user_id):
    return 'Retrieves all of a users projects'


@users.route('/<user_id>/projects/<project_id>', methods=['GET'])
def get_user_project(user_id, project_id):
    return 'get_user_project'


@users.route('/<user_id>/projects/<project_id>', methods=['PUT'])
def update_user_project(user_id, project_id):
    return 'update_user_project'


@users.route('/<user_id>/projects/<project_id>', methods=['DELETE'])
def delete_user_project(user_id, project_id):
    return 'delete_user_project'

#################### Users/Tasks Routes ####################


@users.route('/<user_id>/tasks', methods=['GET'])
def get_all_user_tasks(user_id):
    return 'Retrieves ALL of a users tasks'
