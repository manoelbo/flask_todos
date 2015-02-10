from flask import Flask, render_template, jsonify, url_for, json, Response, make_response, request, abort
import os
 
app = Flask(__name__)    

tasks = [
  	{"task": u"Discuss report with John", 'status': 0, "id": 1},
  	{"task": u"Learn Python", 'status': 0, "id": 2},
    {"task": u"JorgeBen", 'status': 0, "id": 3}
		]

######## INDEX ########
 
@app.route('/')
def home():
  return render_template('index.html')



####### GET ########


@app.route('/todos/api', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


############# POST ########


@app.route('/todos/api', methods=['POST'])
def create_task():
    task = {
        'id': tasks[-1]['id'] + 1,
        'task': request.json['task'],
        'status': 0, 
    }
    tasks.append(task)
    return jsonify({'task': task}), 201


############# POST ########

@app.route('/todos/api/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

############## PUT ############

@app.route('/todos/api<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})






 
if __name__ == '__main__':
  app.run(debug=True)