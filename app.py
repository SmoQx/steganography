import pathlib
from werkzeug.utils import safe_join
from flask import Flask, render_template, request, redirect, url_for, send_file
import os
from encoder import file_encoder
from decoder import decode_file


app = Flask(__name__)

UPLOAD_FOLDER = 'downloads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['static_url_path'] = '/static'
app.config['static_folder'] = 'static'
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
PASSWORD = 'your_password'  # Change this to your desired password


# Check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    password = request.form.get('password')
    text_to_encrypt = request.form.get('text_to_encrypt')
    encode_flag = request.form.get('upload-action')
    if encode_flag == "encode":
        print("Jebać pis")

    if 'fileInput' not in request.files:
        return redirect(request.url)

    file = request.files['fileInput']
    print(file)

    if file.filename == '' or not allowed_file(file.filename):
        return redirect(request.url)

    if file and encode_flag == "encode":
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        # Encrypt the uploaded file
        encrypted_file_path = file_encoder(pathlib.Path(filename), text_to_encrypt, password)

        return render_template('index.html', filename=encrypted_file_path, password=password)
    elif file and encode_flag == "decode":
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

        print(filename)
        decodeed_text = decode_file(file_path=filename, password=password)

        return render_template('message.html', decoded=decodeed_text)


@app.route('/download/<file_name>')
def download_file(file_name):
    print("tekst")
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
