from werkzeug.utils import secure_filename
from chatbot import get_response_from_file
from flask import Flask, request, render_template, redirect, url_for
import os
import atexit
import shutil
from google.api_core.exceptions import InvalidArgument

app = Flask(__name__, static_url_path='/static')

# configures and mkes upload directory
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@atexit.register
def cleanup_uploads():
    if os.path.exists(UPLOAD_FOLDER):
        shutil.rmtree(UPLOAD_FOLDER)  
        print(f"Cleared uploads folder: {UPLOAD_FOLDER}")


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_text = request.form.get('user_input')
        file = request.files.get('files')
        try:
            # saves uploaded file into upload dir
            if file:
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)

                message = get_response_from_file(file_path, user_text)
                return render_template('index.html', message=message)
            else:
                message = get_response_from_file(False, user_text)
                return render_template('index.html', message=message)
        except InvalidArgument:
            return redirect(url_for('error'))
    else:
        return render_template('index.html')
    
@app.route('/error')
def error():
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)