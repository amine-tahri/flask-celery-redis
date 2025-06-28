from flask import Flask, render_template, jsonify
from tasks import async_task

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask + Celery + Redis is running!"

@app.route("/run-async-task", methods=["POST"])
def run_async_task():
    task = async_task.delay()
    return jsonify({"task_id": task.id}), 202

@app.route("/result/<task_id>")
def get_result(task_id):
    task = async_task.AsyncResult(task_id)
    if task.state == "PENDING":
        return jsonify({"state": task.state, "status": "Task not finished yet"}), 202
    else:
        return jsonify({"state": task.state, "result": task.result }), 200

@app.route('/async-task-template')
def render_async_template():
    return render_template('async_example.html')

if __name__ == "__main__":
    app.run(debug=True)
