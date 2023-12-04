import pathlib
from flask import Flask, render_template, request, redirect, url_for, send_file, safe_join
import os
from encoder import file_encoder
from pathlib import Path


app = Flask(__name__)

UPLOAD_FOLDER = 'downloads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
PASSWORD = 'your_password'  # Change this to your desired password


# Check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    password = request.form.get('password')

    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '' or not allowed_file(file.filename):
        return redirect(request.url)

    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        # Encrypt the uploaded file
        encrypted_file_path = file_encoder(filename)

        return render_template('index.html', filename=encrypted_file_path, password=password)


@app.route('/download/<file_name>')
def download_file(file_name):
    print("kurwaaa!!!")
    encrypted_file_path = safe_join(app.config['UPLOAD_FOLDER'], file_name)
    print(file_name)
    # Ensure the file exists before attempting to send it
    if os.path.exists(encrypted_file_path):
        return send_file(encrypted_file_path, as_attachment=True, download_name=f"{file_name}")
    else:
        return render_template("uploaded.html")


if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
