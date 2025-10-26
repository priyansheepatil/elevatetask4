from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

@app.route('/')
def home():
    return "Welcome!"

@app.route('/users', methods = ['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify(user)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user_id = len(users) + 1
    users[user_id] = {
        'name': data.get('name'),
        'email': data.get('email')
    }
    return jsonify({'message': 'User added successfully', 'user': users[user_id]}), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({'message': 'User not found'}), 404
    data = request.get_json()
    users[user_id]['name'] = data.get('name', users[user_id]['name'])
    users[user_id]['email'] = data.get('email', users[user_id]['email'])
    return jsonify({'message': 'User updated successfully', 'user': users[user_id]})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({'message': 'User not found'}), 404
    del users[user_id]
    return jsonify({'message': 'User deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)