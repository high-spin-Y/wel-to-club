from django.shortcuts import render, redirect

from login import models
from login import forms
from login.viewdir.check import hash_code
# Create your views here.

def register(request):
    register_form_mandatory = [
        "username",
        "password1",
        "password2",
        "first_name",
        "last_name",
        "email",
        "phone",
        "univ",
        "major",
    ]

    if request.session.get('is_login', None):
        return redirect('/index/')

    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = "Please check your input"
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            first_name = register_form.cleaned_data.get('last_name')
            last_name = register_form.cleaned_data.get('first_name')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            phone = register_form.cleaned_data.get('phone')
            univ = register_form.cleaned_data.get('univ')
            major = register_form.cleaned_data.get('major')
            classchoice1 = register_form.cleaned_data.get('classchoice1')
            classchoice2 = register_form.cleaned_data.get('classchoice2')
            classchoice3 = register_form.cleaned_data.get('classchoice3')
            classchoice4 = register_form.cleaned_data.get('classchoice4')
            year_in_school = register_form.cleaned_data.get('year_in_school')
            gender = register_form.cleaned_data.get('gender')

            if password1 != password2:
                message = 'Passwords do not match!'
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:
                    message = 'Username already exists!'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:
                    message = 'Email account already in use!'
                    return render(request, 'login/register.html', locals())

                new_user = models.User()
                new_user.name = username
                new_user.first_name = first_name
                new_user.last_name = last_name
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.phone = phone
                new_user.univ = univ
                new_user.major = major
                new_user.year_in_school = year_in_school
                new_user.classchoice1 = classchoice1
                new_user.classchoice2 = classchoice2
                new_user.classchoice3 = classchoice3
                new_user.classchoice4 = classchoice4
                new_user.gender = gender
                new_user.save()
                return redirect('/login/')
        else:
            print("not valid")
            return render(request, 'login/register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'login/register.html', locals())


