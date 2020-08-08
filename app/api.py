from flask import Blueprint, abort, jsonify, request
from .models import Task, User
from flask_login import login_required, current_user
from . import login_manager

api = Blueprint('api', __name__)

@login_manager.user_loader
def load_user(id):
    return User.get_by_id(id)

@api.route('/getTasksData', methods= ['POST'])
@login_required
def get_task_data():
    print(current_user)
    task_id = request.json['task_id']

    if task_id:
        task = Task.query.get_or_404(task_id)

        if task.user_id != current_user.id:
            abort(404)
        
        dict = {'title' : task.title, 
                'description' : task.description}
        return jsonify(dict)
    else:
        return jsonify({'title' : 'error', 'description' : 'error'})

    
