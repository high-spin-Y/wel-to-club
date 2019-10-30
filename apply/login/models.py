from django.db import models
from login.formdir.formdict import dictionaries
from django.forms import ModelForm
# Create your models here.

class User(models.Model):
    gender = dictionaries("gender_type")
    classchoice = dictionaries("class_type")
    hesfchoice = dictionaries("hesf_type")
    yearinschool = dictionaries("year_type")
    name = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=20, default="")
    last_name = models.CharField(max_length=20, default="")
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, default="")
    univ = models.CharField(max_length=50, default="")
    major = models.CharField(max_length=30, default="")
    year_in_school = models.CharField(max_length=15, choices=yearinschool, default=" ")
    gender = models.CharField(max_length=15, choices=gender, default=" ")
    c_time = models.DateTimeField(auto_now_add=True)
    classchoice1 = models.CharField(max_length=256, choices=classchoice, default="----")
    classchoice2 = models.CharField(max_length=256, choices=classchoice, default="----")
    classchoice3 = models.CharField(max_length=256, choices=classchoice, default="----")
    classchoice4 = models.CharField(max_length=256, choices=classchoice, default="----")
    hesfchoice = models.CharField(max_length=256, choices=hesfchoice, default="----")
    ps_uploaded = models.CharField(max_length=30, default="Ready for upload")
    rl_uploaded = models.CharField(max_length=30, default="Ready for upload")
    md_uploaded = models.CharField(max_length=30, default="Ready for upload")    

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "user"
        verbose_name_plural = "user"

    def class_choice_null(self):
        message = "Please make complete set of class choices."
        complete = "complete"
        if self.classchoice1 == "----":
          return message 
        elif self.classchoice2 == "----":
          return message 
        elif self.classchoice3 == "----":
          return message 
        elif self.classchoice4 == "----":
          return message 
        elif self.hesfchoice == "----":
          return message 
        else:
          return complete

class ClassForm(ModelForm):
    class Meta:
        model = User
        fields = ['classchoice1','classchoice2','classchoice3','classchoice4','hesfchoice']

