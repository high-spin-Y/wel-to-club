from django.shortcuts import render, redirect
from django.http import HttpResponse
from login import models
from login import forms
from django.core.files import File
from login.viewdir.check import upload_null

# Create your views here.
def upload(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    username = request.session.get('user_name')
    user = models.User.objects.get(name=username)
    psmessage = upload_null(user)[0]
    rlmessage = upload_null(user)[1]
    mdmessage = upload_null(user)[2]
    return render(request, 'login/index/upload.html', locals())

