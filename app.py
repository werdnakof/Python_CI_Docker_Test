from flask import Flask
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    text_file = open("dummy.txt", "r")

    line = text_file.readline()

    text_file.close()

#    html = "<h3>Hello {name}! {dummy}</h3>" \
#           "<b>Hostname:</b> {hostname}<br/>" \
#           "<b>Visits:</b> {visits}"
#    return html.format(name=os.getenv("NAME", "world"), dummy=lines, hostname=socket.gethostname(), visits=visits)

    html = "Hello world! {dummy}"
    return html.format(dummy = line)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4545)
