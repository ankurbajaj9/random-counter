# random_number_service.py
import random

from flask import Flask, request, jsonify

from database import get_db

app = Flask(__name__)
db = get_db(app)


class GeneratedNumber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    number = db.Column(db.Integer, nullable=False)


@app.route('/generate-random-number', methods=['POST'])
def generate_random_number():
    data = request.json
    user = data.get('user')
    limit = data.get('limit', 1000)
    if user is None:
        return jsonify({'error': 'User information is required'}), 400

    random_number = random.randint(0, limit)

    # Save to database
    # Save to database
    new_number = GeneratedNumber(username=user, number=random_number)
    db.session.add(new_number)
    db.session.commit()

    return jsonify({'randomNumber': random_number, 'user': user})


@app.route('/get-saved-numbers', methods=['GET'])
def get_saved_numbers():
    numbers = GeneratedNumber.query.all()
    result = [{'id': num.id, 'username': num.username, 'number': num.number} for num in numbers]
    return jsonify({'savedNumbers': result})


def create_table():
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    create_table()
    app.run(host='0.0.0.0', port=5000)
