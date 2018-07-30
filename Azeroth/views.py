from django.shortcuts import render
from django.shortcuts import HttpResponse

from django.contrib import auth
import json

# Create your views here.


def index(request):
    return render(request,'AzerothIndex.html')


def login(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        user = auth.authenticate(username=data['username'],password=data['password'])
        if user is not None:
            auth.login(request,user)
            return HttpResponse(json.dumps({'status_code':200}))
        else:
            return HttpResponse(json.dumps({'status_code':401}))