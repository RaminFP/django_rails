from django.http.response import HttpResponse
import urllib2
import io
import urllib3
import json
import base64
# <name.html>_Controller


def index(request):

    return HttpResponse("Welcome")

def show(request):

    try:
        '''
        # url_rails = 'http://127.0.0.1:3000/'
        # http = urllib2.urlopen(url_rails)
        # return HttpResponse(http.read())
        '''
        http = urllib3.PoolManager()
        url_rails = 'http://127.0.0.1:3000/'
        r = http.request('GET', url_rails)
        b = io.BufferedReader(r, 2048)
        data = b.raw.data
        return HttpResponse(data)

    except Exception as e:

        return HttpResponse("Error %s" % e)

def search(request):

    '''
        # None-Thread Safe request
        name = "ramin"
        url_rails = 'http://127.0.0.1:3000/user/search/%s' % name
        http = urllib2.urlopen(url_rails)
        return HttpResponse(http.read())
    '''
    # Thread Safe request

    try:
        name = "omid"
        http = urllib3.PoolManager()
        url_rails = 'http://127.0.0.1:3000/user/search/%s' % name
        r = http.request('GET', url_rails)
        b = io.BufferedReader(r, 2048)
        data = b.raw.data
        return HttpResponse(data)
    except Exception as e:
        return HttpResponse("Error %s" % e)

def create(request):

    try:
        firstname = "ali"
        lastname = "mahdavi"
        password = "123456"
        confirmpass = '123456'
        email = 'ramin.blackhat@gmail.com'
        is_active = True
        mem_id = 1
        model = {'firstname':firstname,'lastname':lastname,'password':password,'confpassword':confirmpass,'email':email,'is_active':is_active,'mem_id':mem_id}
        json_model = json.dumps(model)
        http = urllib3.PoolManager()
        url_rails = 'http://127.0.0.1:3000/user/create/%s' % base64.b64encode(json_model)
        r = http.request('GET', url_rails)
        b = io.BufferedReader(r, 2048)
        return HttpResponse("Create User Seccuefully")
    except Exception as e:
        return HttpResponse("Error : %s" % e)

def delete(request,id):
    try:
        http = urllib3.PoolManager()
        url_rails = 'http://127.0.0.1:3000/user/delete/%s' % id
        r = http.request('GET', url_rails)
        b = io.BufferedReader(r, 2048)
        return HttpResponse("Delete User Seccuefully")

    except Exception as e:

        return HttpResponse("Error %s " % e)

def edit(request,id):

   try:	
        getEditID = id
        firstname = "ali"
        lastname = "mahdavi"
        password = "123456"
        confirmpass = '123456'
        email = 'ramin.blackhat@gmail.com'
        is_active = True
        mem_id = 1
        model = {'firstname':firstname,'lastname':lastname,'password':password,'confpassword':confirmpass,'email':email,'is_active':is_active,'mem_id':mem_id}
        json_model = json.dumps(model)
        http = urllib3.PoolManager()
        url_rails = 'http://127.0.0.1:3000/user/edit/%s/%s' % (getEditID ,base64.b64encode(json_model))
        r = http.request('GET', url_rails)
        b = io.BufferedReader(r, 2048)
        return HttpResponse("Edit User Seccuefully")
   except Exception as e:

        return HttpResponse("Error %s " % e)

