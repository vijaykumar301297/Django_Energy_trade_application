from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.contrib.auth import login, get_user_model
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.decorators.cache import cache_control
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMessage
from nus_TTS import settings
from django.utils.encoding import force_bytes, force_str
from .tokens import account_activation_token
from .models import Account
from django.contrib.auth.decorators import permission_required
from company.models import Parent, Client

User = get_user_model()


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def user_management(request):
    return render(request, 'usermanagement/usermanagement.html', {'navbar': 'usermanagement'})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def admin(request):
    data = Account.objects.all().filter(role='Admin').order_by('id')
    p = Paginator(data, 10)
    page = request.GET.get("page")
    datas = p.get_page(page)
    
    return render(request, 'userManagement/admin.html', {'data': data, 'datas': datas, 'navbar': 'admin'})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def manager(request):
    data = Account.objects.all().filter(role='Manager').order_by('id')
    p = Paginator(data, 10)
    page = request.GET.get("page")
    datas = p.get_page(page)
    
    return render(request, 'userManagement/manager.html', {'data': data, 'datas': datas, 'navbar': 'manager'})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def user(request):
    data = Account.objects.all().filter(role='User').order_by('id')
    p = Paginator(data, 10)
    page = request.GET.get("page", 1)
    datas = p.get_page(page)
    
    return render(request, 'userManagement/user.html', {'data': data, 'datas': datas, 'navbar': 'user'})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def parent(request):
    data = Account.objects.all().filter(role='Parent').order_by('id')
    p = Paginator(data, 10)
    page = request.GET.get("page", 1)
    datas = p.get_page(page)
    # datas = Paginator.page(page)
    
    return render(request, 'userManagement/parent.html', {'data': data, 'datas': datas, 'navbar': 'parent_user'})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def client(request):
    data = Account.objects.all().filter(role='Client').order_by('id')
    p = Paginator(data, 10)
    page = request.GET.get("page", 1)
    datas = p.get_page(page)
    pc = Client.objects.all()
    return render(request, 'userManagement/client.html',
                  {'data': data, 'datas': datas, 'navbar': 'client_user', 'pc': pc})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def inactive_users(request):
    data = Account.objects.all().filter(is_active=False).order_by('id')
    p = Paginator(data, 10)
    page = request.GET.get("page", 1)
    datas = p.get_page(page)
    # datas = Paginator.page(page)
    
    return render(request, 'userManagement/inactive_user.html', {'data': data, 'datas': datas, 'navbar': 'inactive'})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def user_page(request):
    parent_data = Parent.objects.all()
    client_data = Client.objects.all()
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
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
            myuser = Account(username=username, password=password, email=email, account_status='Invited', role=role,
                             parent_role_id="", client_role_id="")
        
        elif role == "Parent":
            parent_data = Parent.objects.get(id=parent_role)
            myuser = Account(username=username, password="", email=email, account_status='Invited', role=role,
                             parent_role_id=parent_data.id,
                             client_role_id="")
        else:
            parent_data = Parent.objects.get(id=parent_role)
            client_datas = Client.objects.get(id=client_role)
            myuser = Account(username=username, password="", email=email, account_status='Invited', role=role,
                             parent_role_id=parent_data.id,
                             client_role_id=client_datas.id)
        
        myuser.set_password(password)
        myuser.is_active = False
        myuser.save()
        
        current_site = get_current_site(request)
        email_subject = "NUS Account Login credential and Confirm Your Mail"
        message2 = render_to_string('usermanagement/mail.html', {
            'name': myuser.username,
            'password': '12345678',
            'role': myuser.role,
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
    
    return render(request, 'usermanagement/userdata.html', {'data': parent_data, 'client': client_data})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def client_data(request):
    # parent = Parent.objects.all(id = 'parentId')
    if request.method == "POST":
        parentId = request.POST['parentId']
        try:
            parent = Parent.objects.filter(id=parentId).first()
            client = Client.objects.filter(parent_data_id=parentId)
        except Exception:
           return HttpResponse('No Data found')
        return JsonResponse(list(client.values('id', 'client')), safe=False)


def activate_user(request, uidb64, token):
    # User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = Account.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.account_status = 'Confirmed'
        user.save()
        login(request, user)
        
        return render(request, 'home.html')
    
    else:
        return HttpResponse('Activation link is invalid!')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def addclientcompany(request):
    data = Parent.objects.all()
    return render(request, 'usermanagement/userdata.html', {'data': data})
    # return render(request,'addParent/addclientcompany.html',)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def edituser(request, id):
    user = Account.objects.get(pk=id)
    context = {
        'user': user,
    }
    
    if request.method == 'POST':
        user.username = request.POST['username']
        # email = email
        user.save()
        
        return redirect('usermanagement/admin')
    
    return render(request, 'usermanagement/edituser.html', context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def moveuser(request, id):
    user = Account.objects.get(pk=id)
    context = {
        'user': user,
    }
    if request.method == 'POST':
        # user.username = request.POST['username']
        user.role = request.POST['role']
        # email = email
        user.save()
        
        return redirect('usermanagement/admin')
    
    return render(request, 'usermanagement/moveuser.html', context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def disableuser(request, id):
    user = Account.objects.get(pk=id)
    context = {
        'user': user,
    }
    
    if request.method == 'POST':
        user.username = request.POST['username']
        user.is_active = False
        user.save()
        
        return redirect('usermanagement/admin')
    
    return render(request, 'usermanagement/disableuser.html', context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def activeuser(request, id):
    user = Account.objects.get(pk=id)
    context = {
        'user': user,
    }
    
    if request.method == 'POST':
        user.username = request.POST['username']
        user.is_active = True
        user.save()
        
        return redirect('usermanagement/admin')
    
    return render(request, 'usermanagement/disableuser.html', context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def moveparentuser(request, id):
    print(id)
    user = Account.objects.get(pk=id)
    parent = Parent.objects.all().exclude(parent=user.parent_role.parent)
    client = Client.objects.all().filter(parent_data_id=user.parent_role.id)
    context = {
        'user': user,
        'parent': parent,
        'client': client
    }
    #
    if request.method == 'POST':
        user.email = request.POST['email']
        user.role = request.POST['role']
        user.parent_role_id = request.POST['parent_role']
        user.client_role_id = request.POST['client_role']
        # email = email
        user.save()

        return redirect('usermanagement/admin')

    return render(request, 'usermanagement/moveparent.html', context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def moveclientuser(request, id):
    print(id)
    user = Account.objects.get(pk=id)
    parent = Parent.objects.all().exclude(parent=user.parent_role.parent)
    client = Client.objects.all().filter(parent_data_id=user.parent_role.id)
    context = {
        'user': user,
        'parent': parent,
        'client': client
    }

    if request.method == 'POST':
        user.email = request.POST['email']
        user.role = request.POST['role']
        user.parent_role_id = request.POST['parent_role']
        user.client_role_id = request.POST['client_role']
        # email = email
        user.save()

        return redirect('usermanagement/admin')

    return render(request, 'usermanagement/moveclient.html', context)
