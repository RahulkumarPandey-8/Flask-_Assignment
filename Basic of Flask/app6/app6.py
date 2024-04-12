# Q6. Build a Flask app that allows users to upload files and display them on the website.


from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import os

app6 = Flask(__name__)

# Function to create the uploads folder if it doesn't exist
def create_upload_folder():
    if not os.path.exists('uploads'):
        os.makedirs('uploads')

# Call the function to create the folder
create_upload_folder()

# Configure upload folder and allowed extensions
app6.config['UPLOAD_FOLDER'] = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app6.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if file is selected
        if 'file' not in request.files:
            flash('No file selected')
            return redirect(request.url)

        file = request.files['file']
        # Check if file is empty
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        # Check allowed file extension
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app6.config['UPLOAD_FOLDER'], filename))
            # Display uploaded file path
            return f"File uploaded successfully! <br> File path: {os.path.join(app6.config['UPLOAD_FOLDER'], filename)}"
        else:
            flash('Invalid file format. Allowed extensions: ' + ', '.join(ALLOWED_EXTENSIONS))
            return redirect(request.url)

    return render_template('upload_form.html')

if __name__ == '__main__':
    app6.run(debug=True)
