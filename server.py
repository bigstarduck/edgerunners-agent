from flask import Flask, request, send_from_directory

# creates a Flask application 
app = Flask(__name__) 

from models import character

# @app.route("/") 
# def hello(): 
#     return "Hello World"

@app.route('/')
def index():
    return "<a href=index.html>Click Me Now</a>"

#Serves the static pages
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/get_character_data')
def send_character_data():
    return character.get_character_data()

@app.route('/set_health', methods = ['POST', 'GET'])
def set_health():
    if request.method == 'POST':
        body = request.get_json()
        # print(body)
        id = body['id']
        hp = body['hp']
        timestamp = body['timestamp']

    else:
        id = request.args.get('id')
        hp = request.args.get('hp')
        timestamp = request.args['timestamp']

    return character.set_health(id, hp, timestamp)

@app.route('/set_armor', methods = ['POST', 'GET'])
def set_armor():
    if request.method == 'POST':
        body = request.get_json()
        id = body['id']
        hp = body['hp']
        timestamp = body['timestamp']
    else:
        id = request.args.get('id')
        hp = request.args.get('hp')
        timestamp = request.args['timestamp']

    return character.set_armor(id, hp, timestamp)

# run the application 
if __name__ == "__main__": 
    app.run(debug=True)
