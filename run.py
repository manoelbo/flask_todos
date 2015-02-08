from flask import Flask, render_template, jsonify, url_for, json, Response, make_response, request
import os
 
app = Flask(__name__)    



######## INDEX ########
 
@app.route('/')
def home():
  return render_template('index.html')


####### GET ########

@app.route('/todos/api', methods=['GET'])
def get_tasks():
	tasks = [
  		{"task": u"Do the Laundry"},
  		{"task": u"Learn Python"}
	]
	return Response(json.dumps(tasks),  mimetype='application/json')
    


 ####### POST ########

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    tasks = {
        'task': request.json.get('task', ""),
    }

    return Response(json.dumps(tasks),  mimetype='application/json')












 
if __name__ == '__main__':
  app.run(debug=True)