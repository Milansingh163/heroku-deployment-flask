from flask import Flask
from flask import request
import os

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return 'Welcome to ABC Corporation'


@app.route('/greet')
def greet():
    return 'HELLO WORLD'


@app.route('/name')
def get_name():
    data = request.args.get('val')
    return 'my name is {}'.format(data)


if __name__ =='__main__':
     app.run(debug=True, port=os.getenv("PORT", default=5000))