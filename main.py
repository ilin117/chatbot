from chatbot import get_response_from_picture
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        picture = request.files['files']
        user_text = request.form.get('user_input')
        message = get_response_from_picture(picture, user_text)
        return render_template('index.html', message=message)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)