# random_number_service.py
from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/generate-random-number', methods=['GET'])
def generate_random_number():
    limit = int(request.args.get('limit', 1000))
    random_number = random.randint(0, limit)
    return jsonify({'randomNumber': random_number})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)