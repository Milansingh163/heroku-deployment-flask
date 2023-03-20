from flask import Flask
from flask import request
from flask import url_for
import os

app = Flask(__name__)

@app.route('/')
def home_page():
    return 'Company Name: ABC <br>Corporation Location: India <br>Contact Detail: 999-999-9999'

@app.route('/welcome')
def welcome():
    return 'Welcome to ABC Corporation'


@app.route('/greet')
def greet():
    return 'Hello World !!'
@app.route('/user/<name>')
def username(name):
    return 'The name of the user is {}'.format(name)

with app.test_request_context():
    print(url_for('welcome'))
    print(url_for('greet'))
    print(url_for('username',name='Milan'))

if __name__ =='__main__':
     app.run(debug=True, port=os.getenv("PORT", default=5000))