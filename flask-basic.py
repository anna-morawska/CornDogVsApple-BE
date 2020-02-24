from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        request_payload = request.get_json()
        return jsonify({'request_payload': request_payload}), 201
    else:
        return jsonify({'data': 'Hello World'})

@app.route('/multiply/<int:num>', methods=['GET'])
def multiply(num):
   return jsonify({'data': num*10})

if __name__ == "__main__":
    app.run(debug=True)
