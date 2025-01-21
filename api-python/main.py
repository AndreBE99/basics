from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello():
  return 'Hello, World!'

@app.route('/users/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def get_user(user_id):
  user = {'id': user_id, 'name': 'test', 'phone': '123456789'}
  query = request.args.get('query')
  if query:
    user['query'] = query

  # GET Request
  if request.method == 'GET':
    return jsonify(user), 200

  # PUT Request to update user data
  elif request.method == 'PUT':
    data = request.get_json()
    user.update(data)  # Update user dictionary with data from request
    return jsonify(user), 200

  # DELETE Request to remove user
  elif request.method == 'DELETE':
    return jsonify({'message': f'User {user_id} deleted'}), 204

@app.route('/users', methods=['POST'])
def create_user():
  data = request.get_json()
  data['status'] = 'user created'
  return jsonify(data), 201

if __name__ == '__main__':
  app.run(debug=True)