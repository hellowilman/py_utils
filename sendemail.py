# coding=utf-8
__author__ = 'Wilman WZ'

# 你好
import smtplib
from email.mime.text import MIMEText


class SendEmail(object):
    server = None
    you = None
    ac  = None
    pwd = None

    def __init__(self,SMTPHost):
        self.host = SMTPHost
        self.server = smtplib.SMTP(SMTPHost)
        self.server.starttls()

    def login(self,ac,pwd):
        if self.server :
            try:
                self.server.login(ac,pwd)
                self.ac = ac
                self.pwd = pwd
            except Exception as e:
                print e
                return False
            return True
        else:
            return False

    def send(self,to_addrs, subject, msg, you = None):
        if self.server:
            if not you:
                you = self.you
            else:
                self.you = you
            if not you:
                you = "sendemail@nodomain.com"
            Mmsg = MIMEText(msg)
            Mmsg['Subject'] = subject
            Mmsg['From'] = you
            Mmsg['To'] = ','.join(to_addrs)
            try:
                self.server.sendmail(self.you,to_addrs,Mmsg.as_string())
            except Exception as e:
                print e
                return False
            return True
        else:
            return False

    def close(self):
        if self.server:
            self.server.quit()

class GmailSendEmail(SendEmail):
    def __init__(self,ac,pwd):
        super(GmailSendEmail,self).__init__("smtp.gmail.com:587")
        if self.server.login(ac,pwd):
            print "Initial Gmail succeeded!"
        else:
            print "Initial Gmail failed!"

def send_bfs_email(email):
    gmsrv=GmailSendEmail("bfschoolhk","bfs@2014!")
    gmsrv.send([email],'BFS Email','This is a BFS email for ' + email)
    return 0


