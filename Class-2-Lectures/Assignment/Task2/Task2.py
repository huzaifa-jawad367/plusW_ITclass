from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import random
app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
  return render_template('index.html')



