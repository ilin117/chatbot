from chatbot import get_response_from_picture
from flask import Flask, request, render_template, redirect, url_for
from PIL import UnidentifiedImageError

app = Flask(__name__, static_url_path='/static')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_text = request.form.get('user_input')
        # if no picture is uploaded, only send in text
        if bool(request.files['image']) == False:
            message = get_response_from_picture(False, user_text)
        else:
            try:
                picture = request.files['image']
                message = get_response_from_picture(picture, user_text)
            except UnidentifiedImageError:
                return redirect(url_for('error'))
        return render_template('index.html', message=message)
    else:
        return render_template('index.html')
    
@app.route('/error')
def error():
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)

