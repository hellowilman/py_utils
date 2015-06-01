from flask import Flask, request, send_from_directory
from rq import Queue
from redis import Redis
from my_email_jobtask import sendemail_task
import simplejson as json

q = Queue(connection = Redis())

app = Flask(__name__,static_url_path='/static')

def get_param(r,k):
    v = r.args.get(k,None)
    if not v:
        v = r.form.get(k,None)
    return v

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/sendemail/callback/',methods=["POST","GET"])
def sendemail_callback():
    print request.method
    print request.form
    return 'this is wilman hello'

@app.route('/sendemail/send/',methods=["GET","POST"])
def sendemail():
    id = get_param(request,"id")
    to = get_param(request,"to")
    if to:
        to = json.loads(to)
    fr = get_param(request,"from")
    msg = get_param(request,"msg")
    sub = get_param(request,"subject")
    url = get_param(request,"url")
    try:
        data = {
        "id":id,
        "to":to,
        "from":fr,
        "msg":msg,
        "subject":sub,
        "url":url
        }
        q.enqueue(sendemail_task, data)
    except Exception as e:
        print e
    return "hello wilman send!"

@app.route("/test.html")
def test():
    return app.send_static_file('test.html')

if __name__ == '__main__':
    app.run()
