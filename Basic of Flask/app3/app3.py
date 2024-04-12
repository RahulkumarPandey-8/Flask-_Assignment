
# Q3. Develop a Flask app that uses URL parameters to display dynamic content.


from flask import Flask, request

app3 = Flask(__name__)

@app3.route('/')
def index():
    return 'Welcome to my Flask app!'

@app3.route('/greet')
def greet():
    name = request.args.get('name', 'Guest')
    return f'Hello, {name}!'

if __name__ == '__main__':
    app3.run(debug=True)
