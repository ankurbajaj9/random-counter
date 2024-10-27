# random_number_service.py
import random

from flask import Flask, request, jsonify

from common.database import get_db
from common.user import User

app = Flask(__name__)
db = get_db(app)


class GeneratedNumber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, nullable=False)
    limit = db.Column(db.Integer, nullable=False)
    number = db.Column(db.Integer, nullable=False)


@app.route('/generate-random-number', methods=['POST'])
def generate_random_number():
    data = request.json
    user = data.get('user')
    limit = data.get('limit', 1000)
    user_data = User.query.filter_by(name=user).first()
    if user is None:
        return jsonify({'error': 'User information is required'}), 400
    elif user_data is None:
        return jsonify({'error': 'User not found. Please generate a user first'}), 400

    random_number = random.randint(0, limit)

    # Save to database
    new_number = GeneratedNumber(userid=user_data.id, number=random_number, limit=limit)
    db.session.add(new_number)
    db.session.commit()

    return jsonify({'randomNumber': random_number, 'user': user})


@app.route('/get-saved-numbers', methods=['GET'])
def get_saved_numbers():
    numbers = GeneratedNumber.query.all()
    result = [{'id': num.id, 'username': User.query.get(num.userid).name, 'number': num.number, 'limit': num.limit} for num in numbers]
    return jsonify({'savedNumbers': result})


def create_table():
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    create_table()
    app.run(host='0.0.0.0', port=5000)
