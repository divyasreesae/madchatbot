from http.client import HTTPConnection
from base64 import b64encode
import json 
BASE_URL = 'http://testing.makeadiff.in/api/v1'
auth = ('api@makeadiff.in', 'temp-password')

def getUserData():
    c = HTTPConnection("testing.makeadiff.in")
    userAndPass = b64encode(b"api@makeadiff.in:temp-password").decode("ascii")
    headers = { 'Authorization' : 'Basic %s' %  userAndPass }
    c.request('GET', '/api/v1/users', headers=headers)
    res = c.getresponse()
    result = res.read()
    data = json.loads(result)['data']
    return data

def get_credits(userid):
    c = HTTPConnection("testing.makeadiff.in")
    userAndPass = b64encode(b"api@makeadiff.in:temp-password").decode("ascii")
    headers = { 'Authorization' : 'Basic %s' %  userAndPass }
    resource = '/users/{}/credit'.format(userid)
    c.request('GET', '/api/v1'+resource, headers=headers)
    res = c.getresponse()
    result = res.read()
    data = json.loads(result)['data']['credit']
    return data


def get_class_history(userid):
    c = HTTPConnection("testing.makeadiff.in")
    userAndPass = b64encode(b"api@makeadiff.in:temp-password").decode("ascii")
    headers = { 'Authorization' : 'Basic %s' %  userAndPass }
    resource = '/users/{}/past_classes'.format(userid)
    c.request('GET', '/api/v1'+resource, headers=headers)
    res = c.getresponse()
    result = res.read()
    data = json.loads(result)['data']['classes']
    return data