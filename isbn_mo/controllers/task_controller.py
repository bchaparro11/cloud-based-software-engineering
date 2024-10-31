from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from services.task_service import TaskService

task_blueprint = Blueprint('tasks', __name__)

@task_blueprint.route('/tasks', methods=['POST'])
def create_task():

    data = request.form
    name = data.get('name')
    description = data.get('description')

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    TaskService.create_task(name, description)
    return redirect(url_for('tasks.index'))

@task_blueprint.route('/')
def index():
    return render_template('index.html')

@task_blueprint.route('/get_tasks')
def get_tasks():
    tasks = TaskService.get_all_tasks_service()
    holder = {}
    for task in tasks:
        holder[task.id]=[task.name,task.description]
    return holder

@task_blueprint.route('/update_task')
def update_task():
    return render_template("update_task.html")

@task_blueprint.route('/update',methods=['POST'])
def update():
    data = request.form
    id =  data.get('id')
    name = data.get('name')
    description = data.get('description')

    TaskService.update_task_service(id,name, description)
    return redirect(url_for('tasks.index'))