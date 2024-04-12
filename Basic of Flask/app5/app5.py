#Q 5. Implement user sessions in a Flask app to store and display user-specific data.

from flask import Flask, render_template, request, session, redirect, url_for

app5 = Flask(__name__)
app5.secret_key = '7452d003c3bf4438223322dbb5fa662b'

@app5.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('submit'))
    return render_template('index.html')

@app5.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        session['username'] = request.form['name']
        return redirect(url_for('submit'))
    return render_template('submit.html', name=session.get('username'))

@app5.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app5.run(debug=True)
