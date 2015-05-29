#-*- coding: utf-8 -*-
__author__ = 'Wilman WZ'
import simplejson as json

def ok_json(data):
    try:
        s =  json.dumps({"ok":True,"data":data})
        return s
    except Exception as e:
        print e
        return None

def fail_json(errmsg,data = None):
    try:
        s =  json.dumps({"ok":False,"data":data,"errmsg":errmsg})
        return s
    except Exception as e:
        print e
        return None
