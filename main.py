from flask import Flask
from flask import request
import os

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def hello_world():
    return 'This is my home page'

@app.route('/name')
def get_name():
    data = request.args.get('val')
    return 'my name is {}'.format(data)


if __name__ =='__main__':
     app.run(debug=True, port=os.getenv("PORT", default=5000))