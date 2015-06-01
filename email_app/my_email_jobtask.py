__author__ = 'wilman'

from sendemail import GmailSendEmail
import urllib2,urllib

def sendemail_task(data):
    id = data.get("id",None)
    to = data.get("to",None)
    fr = data.get("from",None)
    msg = data.get("msg",None)
    sub = data.get("subject","No Title Email")
    callback_url = data.get("url",None)
    if not to or not msg:
        return None
    err_msg = ""
    try:
        gs = GmailSendEmail("wilmanhello","hello@wilman1234")
        send_ok = gs.send(to,sub,msg,fr)
    except Exception as e:
        err_msg = err_msg + str(e)
        send_ok  = False

    if callback_url:
        if send_ok:
            back_msg = "email send successed "

        else:
            back_msg = "Email send failed! " + err_msg
        try:
            params = urllib.urlencode({"id":id,"result": send_ok,"msg":back_msg})
            req = urllib2.Request(callback_url,params)
            rsp = urllib2.urlopen(req)
            return rsp.read()

        except Exception as e:
            print "Error on callback: "+ str(e)


