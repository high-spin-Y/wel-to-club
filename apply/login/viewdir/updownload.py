from django.shortcuts import render, redirect
from django.http import HttpResponse
from login import models
from login import forms
from django.core.files import File
import os

# Create your views here.

def return_save_dir(username):
    upload_dir = r'/*********/'
    saved_file_dir = os.path.join(upload_dir, username) 
    if not os.path.exists(saved_file_dir):
        os.makedirs(saved_file_dir)
    return saved_file_dir

def handle_uploaded_file(f, saved_file_dir, saved_filename):
    file_pathname = os.path.join(saved_file_dir, saved_filename)
    extention = os.path.splitext(saved_filename)[1]
    if extention in [".pdf", ".doc", ".docx", ".PDF", ".DOC", ".DOCX"]:
        with open(file_pathname, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        return 0   
    else: 
        return 1


def download_file(request, filename):
    file_pathname = os.path.join(SAVED_FILES_DIR, filename)
 
    with open(file_pathname, 'rb') as f:
        file = File(f)
 
        response = HttpResponse(file.chunks(),
                                content_type='APPLICATION/OCTET-STREAM')
        response['Content-Disposition'] = 'attachment; filename=' + filename
        response['Content-Length'] = os.path.getsize(file_pathname)

    return response 

