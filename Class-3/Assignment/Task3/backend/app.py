import os
from flask import Flask, send_from_directory, jsonify, request
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

contacts = {}

@app.route('/api/search', methods=['GET'])
def get_contact(name):
    """
    Search Contacts using a Name.
    """
    return jsonify({"Contact": contacts[name]})

@app.route('/api/tasks', methods=['POST'])
def add_contact():
    """
    Expects a JSON payload with a "task" field.
    Example: { "task": "Buy groceries" }
    """
    data = request.get_json()
    if not data or 'contact' not in data:
        return jsonify({"error": "No task provided"}), 400
    contact = data['contact']
    contacts[contact['name']] = contact['contact']

    return jsonify({"message": "Contact added", "contacts": contacts}), 201

# Serve React build
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react_app(path):
    dist_dir = os.path.join(os.path.dirname(__file__), '..', 'frontend', 'dist')

    if path != "" and os.path.exists(os.path.join(dist_dir, path)):
        return send_from_directory(dist_dir, path)
    else:
        # For any other route or if the file doesn't exist, serve index.html
        return send_from_directory(dist_dir, 'index.html')

if __name__ == "__main__":
    app.run(debug=True)
