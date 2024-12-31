from flask import Flask, jsonify, request

app = Flask(_name_)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the DevOps Simple App!"})

@app.route('/api/data', methods=['GET'])
def get_data():
    sample_data = {"id": 1, "name": "DevOps Project", "status": "Active"}
    return jsonify(sample_data)

@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.json
    return jsonify({"message": "Data received!", "data": data}), 201

if _name_ == '_main_':
    app.run(debug=True, host='0.0.0.0', port=5000)
