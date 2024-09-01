from flask import Flask, render_template, send_from_directory

# creates a Flask application 
app = Flask(__name__) 
  
# @app.route("/") 
# def hello(): 
#     return "Hello World"

@app.route('/<path:path>')
def send_report(path):
    return send_from_directory('static', path)

# run the application 
if __name__ == "__main__": 
    app.run(debug=True)
