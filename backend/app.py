from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)

with open('products.json') as f:
    products = json.load(f)

chat_history = []

@app.route('/chat', methods=['POST'])
def handle_chat():
    user_input = request.json.get('message', '').lower()
    response_data = []

    if 'laptop' in user_input:
        response_data = [p for p in products if 'laptop' in p['category'].lower()]
    elif 'smartphone' in user_input or 'phone' in user_input:
        response_data = [p for p in products if 'smartphone' in p['category'].lower()]
    elif 'book' in user_input:
        response_data = [p for p in products if 'book' in p['category'].lower()]
    else:
        response_data = [p for p in products if user_input in p['name'].lower()]

    chat_history.append({
        'timestamp': datetime.now().isoformat(),
        'user': user_input,
        'response': response_data[:5]
    })

    return jsonify(response_data[:5])

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/history', methods=['GET'])
def get_history():
    return jsonify(chat_history)

if __name__ == '__main__':
    app.run(debug=True)
