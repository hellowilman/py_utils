#-*- coding: utf-8 -*-
__author__ = 'Wilman WZ'
import simplejson as json
import hashlib

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

# do rest commands
def rest_post(url,data):
    pass
def rest_get(url,data):
    pass


# flask get_query
def get_query(req,k):
    v = req.GET.get(k,None)
    if not v:
        v = req.POST.get(k,None)
    if not v:
        v = req.FILES.get(k,None)
    return v

# get md5 digest from string
def md5hex(str):
    return hashlib.md5(str).hexdigest()