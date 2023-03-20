from flask import Flask
from flask import request
import os

app = Flask(__name__)

@app.route('/')
def home_page():
    return '''  Company Name: ABC Corporation <br>
                Location: India <br>
                Contact Detail: 999-999-9999'''

@app.route('/welcome')
def welcome():
    return '<h1>Welcome to ABC Corporation</h1>'


@app.route('/greet')
def greet():
    return 'Hello World !!'


@app.route('/name')
def get_name():
    data = request.args.get('val')
    return 'my name is {}'.format(data)


if __name__ =='__main__':
     app.run(debug=True, port=os.getenv("PORT", default=5000))