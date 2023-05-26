from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World'

@app.route('/blog')
def blog():
    return 'Hello World blog page'

app.run(port=5001)
