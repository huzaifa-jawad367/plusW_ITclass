from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

def convert_to_uppercase(input_string):
    return input_string.upper()

def convert_to_lower(input_string):
    return input_string.lower()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process_name', methods=['POST'])
def process_name():
    data = request.json
    first_name = data['firstName']
    last_name = data['lastName']
    case_option_fn = data['FNcaseOption']
    case_option_ln = data['LNcaseOption']

    if case_option_fn == 'uppercase':
        formatted_first = convert_to_uppercase(first_name)
    else:
        formatted_first = convert_to_lower(first_name)

    if case_option_ln == 'uppercase':
        formatted_last = convert_to_uppercase(last_name)
    else:
        formatted_last = convert_to_lower(last_name)

    total_length = len(first_name) + len(last_name)

    return jsonify({
        'firstName': formatted_first,
        'lastName': formatted_last,
        'totalLength': total_length
    })

if __name__ == '__main__':
    app.run(debug=True)
