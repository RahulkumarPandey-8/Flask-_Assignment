# Q1. Create a Flask app that displays "Hello, World!" on the homepage.

from flask import Flask

app1 = Flask(__name__)

@app1.route('/')
def home():
    return "Hello world"

if __name__ == '__main__':
    app1.run(debug=True)


