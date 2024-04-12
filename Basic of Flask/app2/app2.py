
# Q2. Build a Flask app with static HTML pages and navigate between them.


from flask import Flask, render_template

app2 = Flask(__name__)

@app2.route('/')
def index():
    return render_template('index.html')

@app2.route('/page1')
def page1():
    return render_template('page1.html')

@app2.route('/page2')
def page2():
    return render_template('page2.html')

if __name__ == '__main__':
    app2.run(debug=True)  

