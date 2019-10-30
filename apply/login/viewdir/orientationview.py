from django.shortcuts import render, redirect
# Create your views here.

def orientation(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'login/index/Orientation_Pages.htm')	
