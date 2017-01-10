import threading
import time
import urllib2
import datetime
from sendemail import *

URL = 'http://wp2016.bfschool.hk/index.html'
TIME = 5*60 # check every 5 min

def get_time():
    return datetime.datetime.now().strftime("%Y%m%d %H:%M:%S")

def test_web(url):
    ts = get_time()
    try:
        req = urllib2.urlopen(url, timeout=60);
        if req.read():
            print "%s Network OK" %ts
    except Exception as e:
       print "%s Network error: %s" %(ts, e)
#   should send email here
       gmsrv=GmailSendEmail("bfschoolhk","bfs@2014!")
       gmsrv.send(['zwilman+bfs@gmail.com'],'Server Error', "%s %s network error" %(ts,url))

    global web_timer
    web_timer = threading.Timer(TIME, test_web, [URL])
    web_timer.start()

if __name__== "__main__":
    global web_timer
    web_timer = threading.Timer(TIME, test_web, [URL])
    web_timer.start()
