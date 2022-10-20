from flask import Flask
app = Flask(__name__)
#define the starting point -- root
@app.route('/')
def hello_world():
    return 'Hello world'