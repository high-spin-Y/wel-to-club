from django.shortcuts import render, redirect
from django.http import HttpResponse
from login import models
from login import forms
from django.core.files import File
from login.viewdir.check import class_choice_null, upload_null,hesf_choice_null

# Create your views here.
def index(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    username = request.session.get('user_name')
    user = models.User.objects.get(name=username)
#        return render(request, 'login/index.html', locals())
#    downloadform = forms.DownloadFileForm(request.POST, initial={'file':True})
    message = class_choice_null(user)
    hesfmessage = hesf_choice_null(user)
    psmessage = upload_null(user)[0]
    rlmessage = upload_null(user)[1]
    mdmessage = upload_null(user)[2]
    request.session.set_expiry(0)
    return render(request, 'login/index.html', locals())

