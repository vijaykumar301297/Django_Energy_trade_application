from django.core.paginator import Paginator
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth import login
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.decorators.cache import cache_control
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMessage
from nus_TTS import settings
from django.utils.encoding import force_bytes, force_str
from .tokens import account_activation_token
from django.contrib.auth import get_user_model
from company.models import *
from .models import Account
from django.contrib.auth.decorators import permission_required

User = get_user_model()


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def user_management(request):
    return render(request, 'usermanagement/usermanagement.html', {'navbar': 'usermanagement'})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def admin(request):
    data = Account.objects.all().filter(role='Admin')
    p = Paginator(data, 2)
    page = request.GET.get("page")
    datas = p.get_page(page)

    return render(request, 'userManagement/admin.html', {'data': data, 'datas': datas, 'navbar': 'admin'})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def manager(request):
    data = Account.objects.all().filter(role='Manager')
    p = Paginator(data, 10)
    page = request.GET.get("page")
    datas = p.get_page(page)

    return render(request, 'userManagement/manager.html', {'data': data, 'datas': datas, 'navbar': 'manager'})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def user(request):
    data = Account.objects.all().filter(role='User')
    p = Paginator(data, 10)
    page = request.GET.get("page", 1)
    datas = p.get_page(page)
    # datas = Paginator.page(page)

    return render(request, 'userManagement/user.html', {'data': data, 'datas': datas, 'navbar': 'user'})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def parent(request):
    data = Account.objects.all().filter(role='Parent')
    p = Paginator(data, 10)
    page = request.GET.get("page", 1)
    datas = p.get_page(page)
    # datas = Paginator.page(page)

    return render(request, 'userManagement/parent.html', {'data': data, 'datas': datas, 'navbar': 'parent'})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def client(request):
    data = Account.objects.all().filter(role='Client')
    p = Paginator(data, 10)
    page = request.GET.get("page", 1)
    datas = p.get_page(page)
    # datas = Paginator.page(page)

    return render(request, 'userManagement/client.html', {'data': data, 'datas': datas, 'navbar': 'client'})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def user_page(request):
    data = Parent.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password =request.POST['password']
        email = request.POST['email']
        role = request.POST['role']
        parent_role = request.POST['parent_role']
        client_role = request.POST['client_role']

        if Account.objects.all().filter(email=email).exists():
            messages.error(request, 'Email Already available, Kindly proceed with login')
            return redirect('usermanagement/Invite_user')

        elif Account.objects.all().filter(username=username).exists():
            messages.error(request, 'Username Already available, Kindly proceed with login')
            return redirect('usermanagement/Invite_user')

        if role == "Admin" or role == "Manager" or role == "User":
            myuser = Account(username=username, password=password, email=email, role=role, parent_role="", client_role="")
        elif role == "parent_company":
            myuser = Account(username=username, password=password, email=email, role=role, parent_role=parent_role,
                             client_role="")
        else:
            myuser = Account(username=username, password="", email=email, account_status='Invited', role=role,
                             parent_role=parent_role,
                             client_role=client_role)

        myuser.set_password(password)
        myuser.save()

        subject = "Login message"
        message = "Hello " + myuser.username + ','
        from_email = settings.EMAIL_HOST
        to_user = [myuser.email]
        send_mail(subject, message, from_email, to_user, fail_silently=True)

        current_site = get_current_site(request)
        email_subject = "Confirm Your Mail"
        message2 = render_to_string('usermanagement/mail.html', {

            'name': myuser.username,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': account_activation_token.make_token(myuser)
        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST,
            [myuser.email],
        )
        email.fail_silently = True
        email.send()

        return redirect('usermanagement/admin')


    else:
        return render(request, 'usermanagement/userdata.html', {'data': data})


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = Account.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError,):
        myuser = None

    if myuser is not None and account_activation_token.check_token(myuser, token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request, myuser)
        messages.success(request, "Your Account has been activated!!")
        return render('')
    else:
        return HttpResponse('Activation link is invalid!')


# def parent(request, id):
#     parentdata = Parent.objects.get(pk = id)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def addclientcompany(request):
    data = Parent.objects.all()
    return render(request, 'usermanagement/userdata.html', {'data': data})
    # return render(request,'addParent/addclientcompany.html',)
