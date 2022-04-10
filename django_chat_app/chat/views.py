from django.http.response import HttpResponseRedirect
from .models import Message, Chat
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from django.http import JsonResponse

@login_required(login_url='/login')

def index(request):
    """
    This function render the chat messages
    """
    if request.method == 'POST':
        mychat = Chat.objects.get(id=1)
        new_message = Message.objects.create(text=request.POST['textmessage'], chat=mychat, author=request.user, receiver=request.user)
        serialized_obj = serializers.serialize('json', [ new_message, ])
        return JsonResponse(serialized_obj[1:-1], safe=False)
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {'messages': chatMessages})


def login_view(request):
    """
    This function is for the login. If the user exist or not
    """
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
    """
    This function is for the registration. It create the User.
    """
    redirect = request.POST.get('next', '/')
    if request.method == 'POST':
        if request.POST.get('password') == request.POST.get('confirm_password'):
            user = User.objects.create_user(username=request.POST.get('username'), first_name=request.POST.get('first_name'), last_name=request.POST.get('last_name'), 
            email=request.POST.get('email'), password=request.POST.get('password'))
            user.save()
            return HttpResponseRedirect(redirect)
        else:
            return render(request, 'auth/register.html', {'wrongPassword': True})
    return render(request, 'auth/register.html')

def logout_view(request):
    """
    This function is for the Logout. It cancel the connection to the app.
    """
    redirect = request.POST.get('next', '/')
    auth_logout(request)
    return HttpResponseRedirect(redirect)