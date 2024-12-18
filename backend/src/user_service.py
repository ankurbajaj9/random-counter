# user_service.py
from flask import Flask, request, jsonify

from common.user import User
from common.database import get_db

app = Flask(__name__)
db = get_db(app)


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(name=data['name'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'id': new_user.id, 'name': new_user.name}), 201


@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'name': user.name} for user in users])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
