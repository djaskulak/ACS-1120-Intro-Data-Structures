"""Main script, uses other modules to generate sentences."""
from flask import Flask, request, redirect, render_template
from dictogram import Dictogram
from cleanup import cleanup
import twitter
from markov_2nd import Markov

app = Flask(__name__)
chain = Markov(cleanup('./corpus.txt'), 2)

@app.before_first_request
def before_first_request():
    """Runs only once at Flask startup"""
    # TODO: Initialize your histogram, hash table, or markov chain here.
    word_list = cleanup('./corpus.txt')
    histogram = Dictogram(word_list)
    return histogram

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    sentence = chain.walk_chain()
    return render_template('home.html', sentence=sentence)

@app.route('/tweet', methods=['POST'])
def tweet():
    status = request.form['sentence']
    twitter.tweet(status)
    return redirect('/')

if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
