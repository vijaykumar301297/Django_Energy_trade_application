from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.http import urlsafe_base64_encode
# from django.contrib.auth.models import User
from django.views.decorators.cache import cache_control
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from userManagement.models import Account
from nus_TTS import settings
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def home_page(request):
    return render(request, 'home.html')


def home(request):
    return render(request, 'home.html')


@ensure_csrf_cookie
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@csrf_protect
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None and Account.objects.filter(account_status='Confirmed'):
            login(request, user)
            userdata = user.username
            # messages.success(request, f' Welcome {userdata}')
            return redirect('home/')
            # return render(request, 'index.html', {username: userdata})
        elif user is not None and Account.objects.filter(account_status='Invited'):
            messages.error(request, 'Kindly activate account')
            return redirect('login')
        else:
            if Account.objects.filter(username=username).exists():
                messages.error(request, 'username Already available,  kindly click reset the password')
                return redirect('login')
            else:
                messages.error(request, 'Bad Credential')
                return redirect('login')

    return render(request, 'loginpage\login.html')


def logout_user(request):
    logout(request)
    return redirect('login')
