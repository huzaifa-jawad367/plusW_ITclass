import os
from flask import Flask, send_from_directory, jsonify, request
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

tasks = []

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """
    Returns the current list of tasks.
    """
    print("returning tasks")
    return jsonify({"tasks": tasks})

@app.route('/api/tasks', methods=['POST'])
def add_task():
    """
    Expects a JSON payload with a "task" field.
    Example: { "task": "Buy groceries" }
    """
    data = request.get_json()
    if not data or 'task' not in data:
        return jsonify({"error": "No task provided"}), 400
    task = data['task']
    tasks.append(task)
    print('returning added tasks')
    return jsonify({"message": "Task added", "tasks": tasks}), 201

@app.route('/api/tasks', methods=['DELETE'])
def remove_task():
    """
    Expects a JSON payload with a "task" field.
    Example: { "task": "Buy groceries" }
    If the task exists, it will be removed.
    """
    data = request.get_json()
    if not data or 'task' not in data:
        return jsonify({"error": "No task provided"}), 400

    task = data['task']
    print('returning tasks after removal')
    if task in tasks:
        tasks.remove(task)
        return jsonify({"message": "Task removed", "tasks": tasks})
    else:
        return jsonify({"error": "Task not found"}), 404

# Serve React build
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react_app(path):
    dist_dir = os.path.join(os.path.dirname(__file__), '..', 'Task1_frontend', 'dist')

    if path != "" and os.path.exists(os.path.join(dist_dir, path)):
        return send_from_directory(dist_dir, path)
    else:
        # For any other route or if the file doesn't exist, serve index.html
        return send_from_directory(dist_dir, 'index.html')

if __name__ == "__main__":
    app.run(debug=True)
