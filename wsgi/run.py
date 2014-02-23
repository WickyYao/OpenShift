import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/a')
@app.route('/index')
def index():
    return 'Hello World!!!!!!'

@app.route('/fancy')
def fancy():
    return 'Love Fancy!!!!!!'

if __name__ == "__main__":
    app.run(debug = "True")
