from .. import db
from flask import Blueprint, jsonify, request
from ..models import Project, Task

projects = Blueprint('projects', __name__)

#################### Projects Routes ####################


@projects.route('/<project_id>/users', methods=['GET'])
def get_users_in_project(project_id):
    project = Project.query.filter_by(id = project_id).first()
    project_users = project.engineers
    return jsonify(users =[user.to_dict() for user in  project_users])

#################### Projects/Tasks Routes ####################


# Creates a task for a project
@projects.route('/<project_id>/tasks', methods=['POST'])
def create_tasks_in_project(project_id):
    project = Project.query.filter_by(id = project_id).first()
    data = request.get_json()
    task = Task(
        name = data['name'],
        description = data['description'],
        deadline = data['deadline'],
        priority = data['priority'],
        progress = data['progress'],
        project = project
    )
    db.session.add(task)
    project.tasks.append(task)
    db.session.commit()
    return f'Task {task.name} created for project {project.name}'


@projects.route('/<project_id>/tasks/<task_id>', methods=['PUT'])
def update_project_tasks(project_id, task_id):
    project = Project.query.filter_by(id = project_id).first()
    task = Task.query.filter_by(project_id = project_id).first()
    data = request.get_json()
    if task in project.tasks:
        if 'name' in data:
            task.name = data['name']
        if 'deadline' in data:
            task.deadline = data['deadline']
        if 'description' in data:
            task.description = data['description']
        if 'priority' in data:
            task.priority = data['priority']
        if 'progress' in data:
            task.progress = data['progress']
        
        db.session.commit()
        return 'updated task in project'
    else:
        return 'Error'


@projects.route('/<project_id>/tasks/<task_id>', methods=['DELETE'])
def delete_project_tasks(project_id, task_id):
    task = Task.query.filter_by(project_id = project_id).first()
    db.session.delete(task)
    db.session.commit()
    return f'Task with id of {task_id} was deleted from database'
