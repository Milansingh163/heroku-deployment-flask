from flask import Flask
from flask import request

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
    app.debug=True
    app.run(host='localhost',port=5000)