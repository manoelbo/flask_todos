from flask import Flask, render_template, jsonify, url_for, json, Response, make_response, request, abort
import os
 
app = Flask(__name__)    

tasks = [
  	{"task": u"Discuss report with John", 'status': False, "id": 1},
  	{"task": u"Learn Python", 'status': False, "id": 2},
    {"task": u"Buy Milk", 'status': False, "id": 3}
		]

######## INDEX ########
 
@app.route('/')
def home():
  return render_template('index.html')



####### GET ########


@app.route('/todos/api', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/todos/api/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


############# POST ########


@app.route('/todos/api', methods=['POST'])
def create_task():
    task = {
        'id': tasks[-1]['id'] + 1,
        'task': request.json['task'],
        'status': False, 
    }
    tasks.append(task)
    return jsonify({'task': task}), 201




############## PUT ############

@app.route('/todos/api/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    task[0]['task'] = request.json.get('task', task[0]['task'])
    task[0]['status'] = request.json.get('status', task[0]['status'])
    return jsonify({'task': task[0]})






 
if __name__ == '__main__':
  app.run(debug=True)
