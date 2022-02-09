from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
  """To run the Flask server, execute `python app.py` in your terminal.
      To learn more about Flask's DEBUG mode, visit
      https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
  app.run(debug=True, port=5001)