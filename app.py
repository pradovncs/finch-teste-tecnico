from flask import Flask, render_template
from app.controllers.pdf_controller import PDFController

import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
controller = PDFController()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    return controller.upload_files()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)