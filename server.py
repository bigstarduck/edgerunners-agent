from flask import Flask, send_from_directory


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
    print(character.character_data)
    for armor in character.character_data["armor"] :
        print(armor)
    return character.character_data

@app.route('/get_character_stats')
def send_character_stats():
    return character.character_stats

@app.route('/get_character_health')
def send_character_health():
    return character.character_health

@app.route('/get_character_armor')
def send_character_armor():
    return character.character_armor

# run the application 
if __name__ == "__main__": 
    app.run(debug=True)
