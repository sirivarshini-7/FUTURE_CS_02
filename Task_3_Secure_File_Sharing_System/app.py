from flask import Flask, render_template, request, send_file
from encryption import encrypt_file, decrypt_file
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            file_data = file.read()
            encrypted_data = encrypt_file(file_data)
            enc_path = os.path.join(UPLOAD_FOLDER, filename + '.enc')
            with open(enc_path, 'wb') as f:
                f.write(encrypted_data)
            return f"✅ File '{filename}' uploaded and encrypted successfully."
    return render_template('index.html')

@app.route('/download/<filename>', methods=['GET'])
def download(filename):
    enc_path = os.path.join(UPLOAD_FOLDER, filename + '.enc')
    if os.path.exists(enc_path):
        with open(enc_path, 'rb') as f:
            encrypted_data = f.read()
        decrypted_data = decrypt_file(encrypted_data)
        dec_path = os.path.join(UPLOAD_FOLDER, filename)
        with open(dec_path, 'wb') as f:
            f.write(decrypted_data)
        return send_file(dec_path, as_attachment=True)
    return "❌ File not found."

if __name__ == '__main__':
    app.run(debug=True)
