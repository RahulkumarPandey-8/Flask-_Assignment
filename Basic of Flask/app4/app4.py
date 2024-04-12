
# Q4.Create a Flask app with a form that accepts user input and displays it.

from flask import Flask, render_template, request

app4 = Flask(__name__)

@app4.route('/')
def index():
    return render_template('index.html')

@app4.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return render_template("submit.html", name=name)

if __name__ == '__main__':
    app4.run(debug=True)
