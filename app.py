from flask import Flask, render_template, request, redirect, url_for
import os
from encoder import file_encoder
from pathlib import Path


app = Flask(__name__)

UPLOAD_FOLDER = 'downloads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
PASSWORD = 'your_password'  # Change this to your desired password


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    password = request.form.get('password')

    #if password != PASSWORD:
    #    return 'Incorrect password. Upload not allowed.'

    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']



    if file.filename == '':
        return redirect(request.url)

    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        return render_template('/uploaded.html', filename=file, password=password)


if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
