import json
import pathlib
from werkzeug.security import safe_join
from flask import Flask, render_template, request, redirect, url_for, send_file, after_this_request
from flask_mail import Mail, Message
import os
from encoder import file_encoder
from decoder import decode_file


app = Flask(__name__)

UPLOAD_FOLDER = 'downloads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['static_url_path'] = '/static'
app.config['static_folder'] = 'static'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False


# Check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


def email_config(app):

    with open('email.cfg', 'r') as read_config:
        configuration = read_config.read()
        dict_conf = json.loads(configuration)
        for x in dict_conf:
            app.config[x] = str(dict_conf[x])
        print(app.config)

    mail = Mail(app)

    return mail


mail = email_config(app)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    password = request.form.get('password')
    text_to_encrypt = request.form.get('text_to_encrypt')
    encode_flag = request.form.get('upload-action')

    if 'fileInput' not in request.files:
        return redirect(request.url)

    file = request.files['fileInput']

    if file.filename == '' or not allowed_file(file.filename):
        return redirect(request.url)

    if file and encode_flag == "encode":
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        print(text_to_encrypt)
        # Encrypt the uploaded file
        encrypted_file_path = file_encoder(pathlib.Path(filename), text_to_encrypt, password)
        print(pathlib.Path(encrypted_file_path).name)
        return render_template('index.html', fileInput=pathlib.Path(encrypted_file_path).name)
    elif file and encode_flag == "decode":
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        print(file)
        decodeed_text = decode_file(file_path=filename, password=password)
        @after_this_request
        def remove_file(response):
            try:
                os.remove(filename)
            except Exception as error:
                app.logger.error(f"Error deleting file: {error}")
            return response

        return render_template('message.html', decoded=decodeed_text)


@app.route('/download/<filename>')
def download_file(filename):
    encrypted_file_path = safe_join(app.config['UPLOAD_FOLDER'], filename)
    print(correct_file_name := filename)
    print(encrypted_file_path)
    # Ensure the file exists before attempting to send it
    if os.path.exists(encrypted_file_path):

        @after_this_request
        def remove_file(response):
            try:
                os.remove(encrypted_file_path)
            except Exception as error:
                app.logger.error(f"Error deleting file: {error}")
            return response

        return send_file(encrypted_file_path, as_attachment=True)
    else:
        print("doesnot exits")
        return render_template("uploaded.html")


@app.route('/send_email', methods=['POST'])
def send_email():
    recipient_email = request.form.get('recipient_email')
    subject = request.form.get('subject')
    message_body = request.form.get('message_body')
    attached_file = request.files['file_input']

    if allowed_file(attached_file.filename):
        temp_file_path = f'temp/{attached_file.filename}'
        attached_file.save(temp_file_path)

        msg = Message(subject, recipients=[recipient_email])
        msg.body = message_body
        with app.open_resource(temp_file_path) as fp:
            msg.attach(attached_file.filename, 'application/octet-stream', fp.read())
        mail.send(msg)

        # Remove the temporary file
        os.remove(temp_file_path)

        return 'Email sent successfully!'
    else:
        return 'Invalid file type!'


if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
