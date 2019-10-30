from django.shortcuts import render, redirect
from . import models
from . import forms
from login.viewdir import indexview, loginview, registerview, logoutview, psuploadview, rluploadview, mduploadview, orientationview, uploadview, courseview
import os

# Create your views here.


def index(request):
    return indexview.index(request)

def login(request):
    return loginview.login(request)

def register(request):
    return registerview.register(request)

def logout(request):
    return logoutview.logout(request)

def upload(request):
    return uploadview.upload(request)

def course(request):
    return courseview.course(request)

def psupload(request):
    return psuploadview.psupload(request)

def rlupload(request):
    return rluploadview.rlupload(request)

def mdupload(request):
    return mduploadview.mdupload(request)

def orientation(request):
    return orientationview.orientation(request)

