#-*- coding: utf-8 -*-
__author__ = 'Wilman WZ'

from sendemail import GmailSendEmail
from webtools import *
def test_sendemail():
    gs = GmailSendEmail("bfschoolhk","bfs@2014!")
    gs.send(["gdsmile@163.com","wilmansky@yahoo.com"],"this is a test subject 1","hihi, it is wilman1","gdsmile@gmail.com")
    gs.send(["gdsmile@163.com","wilmansky@yahoo.com"],"this is a test subject 2","hihi, it is wilman 2")


def test_webtools():
    print ok_json({"w":"wilman","p":100.56})
    print fail_json("some error!",{"w":"wilman","p":100.56})
    print fail_json("some error 2!")

test_sendemail()