from pickle import TRUE
from django.http import HttpResponseRedirect
from .models import Message, Chat
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required(login_url='/login')

def index(request):
    if request.method == 'POST':
        mychat = Chat.objects.get(id=1)
        Message.objects.create(text=request.POST['textmessage'], chat=mychat, author=request.user, receiver=request.user)
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {'messages': chatMessages})


def login_view(request):
    redirect = request.GET.get('next')
    if request.method == 'POST':
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if user:
            login(request, user)
            return HttpResponseRedirect(request.POST.get('redirect'))
        else:
            return render(request, 'auth/login.html', {'wrongPassword' : True, 'wrongUsername' : True, 'redirect': redirect})
    return render(request, 'auth/login.html', {'redirect': redirect})

def register_view(request):
    redirect = request.POST.get('next', '/')
    if request.method == 'POST':
        if request.POST.get('password') == request.POST.get('confirm_password'):
            user = User.objects.create_user(username=request.POST.get('username'), email=request.POST.get('email'), password=request.POST.get('password'))
            user.save()
            return HttpResponseRedirect(redirect)
        else:
            return render(request, 'auth/register.html', {'wrongPassword': True})
    return render(request, 'auth/register.html')

def logout_view(request):
    logout(request)
    return render(request, 'auth/login.html')