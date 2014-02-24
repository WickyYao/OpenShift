import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/a')
@app.route('/index')
def index():
    return 'oh yeah......'

@app.route('/hello')
def fancy():
    return 'hello!!!'

if __name__ == "__main__":
    app.run(debug = "True")
