# app.py
import json
from flask import Flask, render_template, request, jsonify
from tasks import add

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask + Celery + Redis is running!"

@app.route("/add", methods=["POST"])
def run_add_task():
    # data = request.json
    # x = data.get("x")
    # y = data.get("y")
    x = 2
    y = 3
    task = add.delay(x, y)
    return jsonify({"task_id": task.id}), 202

@app.route("/result/<task_id>")
def get_result(task_id):
    task = add.AsyncResult(task_id)
    if task.state == "PENDING":
        return jsonify({"state": task.state, "status": "Task not finished yet"}), 202
    else:
        return jsonify({"state": task.state, "result": task.result }), 200

@app.route('/sync')
def sync():
    return render_template('sync_example.html')

if __name__ == "__main__":
    app.run(debug=True)
