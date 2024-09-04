from flask import Flask, send_from_directory
from models import character
import json

# creates a Flask application 
app = Flask(__name__) 
  
# @app.route("/") 
# def hello(): 
#     return "Hello World"

@app.route('/')
def index():
    return "<a href=index.html>Click Me Now</a>"

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/get_character_data')
def send_health_data():
    return character.character_data

# run the application 
if __name__ == "__main__": 
    app.run(debug=True)
