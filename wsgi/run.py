import os
from flask import Flask, redirect, jsonify, render_template, request
import redis
import json
import time

app = Flask(__name__)

##rc = redis.Redis(host= os.environ['OPENSHIFT_REDIS_HOST'],
##                 port= os.environ['OPENSHIFT_REDIS_PORT'],
##                 password = os.environ['REDIS_PASSWORD'])
rc = redis.Redis()

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

@app.route('/comet')
def comet():
    ts = request.args.get('ts', time.time())

    cmt = Comet()

    result = cmt.check(ts)
    if result:
        return jsonify(**result)

    time.sleep(1)

    ##passed_time = 0
    ##while passed_time < 30:
    ##    result = cmt.check(ts)
    ##    if result:
    ##        return jsonify(**result)
    ##    passed_time += 1
    ##    time.sleep(1)

    return jsonify(ts=time.time())

class Comet(object):
    def check(self, ts):
        new_data = rc.zrangebyscore('chat_content', ts, '+inf')
        if new_data:
            data = {'content':[]}
            for item in new_data:
                data['content'].append(json.loads(item))
            return dict(data=data, ts=time.time())

if __name__ == "__main__":
    app.run(debug = "True")
