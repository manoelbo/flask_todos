from flask import Flask, render_template, jsonify, url_for, json, Response, make_response, request, abort
import os
 
app = Flask(__name__)    

tasks = [
  	{"task": u"Do the Laundry"},
  	{"task": u"Learn Python"},
    {"task": u"JorgeBen"}
		]

######## INDEX ########
 
@app.route('/')
def home():
  return render_template('index.html')



####### GET ########


@app.route('/todos/api', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/todos/api<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


@app.route('/todos/api', methods=['POST'])
def create_task():
    task = {
        'task': request.json['task'],
    }

    tasks.append(task)
    return jsonify({'task': task}), 201





 
if __name__ == '__main__':
  app.run(debug=True)