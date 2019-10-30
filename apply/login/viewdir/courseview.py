from django.shortcuts import render, redirect
from django.http import HttpResponse
from login import models
from login import forms
from django.core.files import File
from login.viewdir.check import class_choice_null,hesf_choice_null
from login.formdir.formdict import dictionaries

# Create your views here.
def course(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    username = request.session.get('user_name')
    user = models.User.objects.get(name=username)
    message = class_choice_null(user)
    hesfmessage = hesf_choice_null(user)
    classchoice_form = forms.IndexForm(request.POST) #initial={'classchoice1':user.classchoice1, 'classchoice2':user.classchoice2, 'classchoice3':user.classchoice3, 'classchoice4':user.classchoice4})
    if classchoice_form.is_valid():
        if 'submit_choice1' in request.POST:
            classchoice1 = classchoice_form.cleaned_data.get('classchoice1')
            user.classchoice1 = classchoice1
        elif 'submit_choice2' in request.POST:        
            classchoice2 = classchoice_form.cleaned_data.get('classchoice2')
            user.classchoice2 = classchoice2
        elif 'submit_choice3' in request.POST:
            classchoice3 = classchoice_form.cleaned_data.get('classchoice3')
            user.classchoice3 = classchoice3
        elif 'submit_choice4' in request.POST:
            classchoice4 = classchoice_form.cleaned_data.get('classchoice4')
            user.classchoice4 = classchoice4
        elif 'submit_choice5' in request.POST:
            hesfchoice = classchoice_form.cleaned_data.get('hesfchoice')
            user.hesfchoice = hesfchoice
        user.save()
        message = class_choice_null(user)
        hesfmessage = hesf_choice_null(user)
    else:
#        classchoice_form = models.ClassForm()
        classchoice_form = forms.IndexForm()
    return render(request, 'login/index/course.html', locals())

