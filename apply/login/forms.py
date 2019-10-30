from django import forms
from captcha.fields import CaptchaField
from login.formdir.formdict import dictionaries

class UserForm(forms.Form):
    username = forms.CharField(label="Username", max_length=15, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Username",'autofocus': ''}))
    password = forms.CharField(label="Password", max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': "Password"}))
    captcha = CaptchaField(label='Please enter the letters:')

class IndexForm(forms.Form):
    genders = dictionaries("gender_type")
    class_choice = dictionaries("class_type")
    hesf_choice = dictionaries("hesf_type")
    yearinschool = dictionaries("year_type")
    classchoice1 = forms.ChoiceField(label='first class choice', choices=class_choice)
    classchoice2 = forms.ChoiceField(label='second class choice', choices=class_choice)
    classchoice3 = forms.ChoiceField(label='third class choice', choices=class_choice)
    classchoice4 = forms.ChoiceField(label='fourth class choice', choices=class_choice)
    hesfchoice = forms.ChoiceField(label='fifth class choice', choices=hesf_choice)

class RegisterForm(forms.Form):
    genders = dictionaries("gender_type")
    classchoice = dictionaries("class_type")
    hesf_choice = dictionaries("hesf_type")
    yearinschool = dictionaries("year_type")
    username = forms.CharField(label="username", max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label="first name", max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="last name", max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="enter password", max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="repeat password", max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="email address", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label="phone number", max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    univ = forms.CharField(label="your university", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    major = forms.CharField(label="your major", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    year_in_school = forms.ChoiceField(label='year in school', choices=yearinschool)
    classchoice1 = forms.ChoiceField(label='first class choice', choices=classchoice)
    classchoice2 = forms.ChoiceField(label='second class choice', choices=classchoice)
    classchoice3 = forms.ChoiceField(label='third class choice', choices=classchoice)
    classchoice4 = forms.ChoiceField(label='fourth class choice', choices=classchoice)
    hesfchoice = forms.ChoiceField(label='fifth class choice', choices=hesf_choice)
    gender = forms.ChoiceField(label='gender', choices=genders)
#    captcha = CaptchaField(label='captcha')


class UploadFileForm(forms.Form):
    file = forms.FileField()

class DownloadFileForm(forms.Form):
    file = forms.BooleanField(initial=True)



