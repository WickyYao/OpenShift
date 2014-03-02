import os
from flask import Flask, redirect, jsonify, render_template, request
import redis
import json
import time

app = Flask(__name__)

rc = redis.Redis(host= OPENSHIFT_REDIS_HOST, port= OPENSHIFT_REDIS_PORT)
##rc = redis.Redis(host= 127.6.26.2, port= 16379, db=0)
##rc = redis.Redis()

@app.route('/')
@app.route('/a')
@app.route('/index')
def index():
    room_content = reversed(rc.zrevrange('chat_content', 0, 200, withscores=True))
    room_content_list = []
    for item in room_content:
        room_content_list.append(json.loads(item[0]))
    return render_template('room.html',room_content = room_content_list)

@app.route('/hello')
def fancy():
    return 'hello!!!'

@app.route('/post_content', methods=['POST'])
def post_content():
    data = {
            'content': request.form.get('content', ''),
            'created': time.strftime('%m-%d %H:%M:%S'),
            }
    rc.zadd('chat_content', json.dumps(data), time.time())
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = "True")
