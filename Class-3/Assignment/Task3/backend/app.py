import os
from flask import Flask, send_from_directory, jsonify, request
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

contacts = {}

@app.route('/api/search', methods=['GET'])
def get_contact():
    """
    Search Contacts using a Name provided as a query parameter.
    Example: /api/search?name=John
    """
    name = request.args.get('name')
    if not name:
        return jsonify({"error": "No name provided"}), 400
    if name not in contacts:
        return jsonify({"error": "Contact not found"}), 404
    return jsonify({"contact": contacts[name]})

@app.route('/api/contact', methods=['POST'])
def add_contact():
    """
    Expects a JSON payload with a "contact" field.
    Example: { "contact": { "name": "John", "contact": "123-456-7890" } }
    """
    data = request.get_json()
    if not data or 'contact' not in data:
        return jsonify({"error": "No contact provided"}), 400

    contact = data['contact']
    if 'name' not in contact or 'contact' not in contact:
        return jsonify({"error": "Missing name or contact information"}), 400

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
