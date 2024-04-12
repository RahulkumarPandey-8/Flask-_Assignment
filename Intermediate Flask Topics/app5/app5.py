
# Q10. Design a Flask app with proper error handling for 404 and 500 errors.

from flask import Flask, render_template

app5 = Flask(__name__)

# Route for handling 404 error (Page Not Found)
@app5.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# Route for handling 500 error (Internal Server Error)
@app5.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500

# Sample route for testing
@app5.route('/')
def index():
    return "Hello, Flask!"

if __name__ == '__main__':
    app5.run(debug=True)
