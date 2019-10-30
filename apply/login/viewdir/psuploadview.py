from django.shortcuts import render, redirect
from django.http import HttpResponse
from login import models
from login import forms
from login.viewdir.updownload import return_save_dir, handle_uploaded_file, download_file
from login.viewdir.check import upload_null
import os
# Create your views here.

def psupload(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    username = request.session.get('user_name')
    user = models.User.objects.get(name=username)
    saved_dir = return_save_dir(username)    
    PSform = forms.UploadFileForm(request.POST, request.FILES)
    if PSform.is_valid():
        f = request.FILES['file']
        f = str(f)
        psname = "PS_%s%s"%(username, os.path.splitext(f)[1]) #rename the uploaded file as PS_username.extendname
        psname = os.path.join(saved_dir, psname) #rewrite with directories
        error = handle_uploaded_file(request.FILES['file'], saved_dir, psname)
        if error == 0:
            user.ps_uploaded = f
            user.save()
            message = "File uploaded successfully!"
        else:
            user.ps_uploaded = "Ready for upload"
            user.save()
            PSform = forms.UploadFileForm()
            message = "Please upload a pdf, doc or docx file!"
    else:
        PSform = forms.UploadFileForm()    
    psmessage = upload_null(user)[0]
    return render(request, 'login/index/psupload.html', locals())
		
