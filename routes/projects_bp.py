from flask import Blueprint

projects = Blueprint('projects', __name__)

#################### Projects Routes ####################


@projects.route('/<project_id>/users', methods=['GET'])
def get_users_in_project(project_id):
    return 'Retrieves all the users working on a project'

#################### Projects/Tasks Routes ####################


@projects.route('/<project_id>/tasks', methods=['POST'])
def create_tasks_in_project(project_id):
    return 'Creates a task for a project'


@projects.route('/<project_id>/tasks/<task_id>', methods=['PUT'])
def update_project_tasks(project_id, task_id):
    return 'Updates a projects tasks'


@projects.route('/<project_id>/tasks/<task_id>', methods=['DELETE'])
def delete_project_tasks(project_id, task_id):
    return 'Deletes tasks'
