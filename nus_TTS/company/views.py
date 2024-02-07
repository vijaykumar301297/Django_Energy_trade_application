from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.cache import cache_control
from .models import Parent, Client
from django.shortcuts import render, redirect


# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def addcompany(request):
    return render(request, 'addParent/addParent.html', {'navbar': 'createcompany'})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def parent(request):
    data = Parent.objects.all()
    datas = Client.objects.all().count()
    return render(request, 'addParent/parent.html', {'data': data, 'navbar': 'parent'})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def addparentcompany(request):
    if request.method == 'POST':
        parent = request.POST['parent']
        if parent == '':
            messages.error(request, 'Enter Parent company')
            return render(request, 'addParent/addparentcompany.html')
        elif Parent.objects.all().filter(parent=parent).exists():
            messages.error(request, 'Company Already Available')
            return render(request, 'addParent/addparentcompany.html')
        else:
            parent_data = Parent(parent=parent)

        parent_data.save()
        return redirect(createcompany)

    else:
        return render(request, 'addParent/addparentcompany.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def client(request):
    data = Client.objects.all()
    return render(request, 'addParent/client.html', {'data': data, 'navbar': 'client'})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def addclientcompany(request):
    data = Parent.objects.all()
    if request.method == 'POST':
        parent_company = request.POST['parent_company']
        client = request.POST['client']
        country = request.POST['country']
        # parent_company = request.POST['parent_company']

        if parent_company == '':
            messages.error(request, 'Enter Parent company')
            return render(request, 'addParent/addclientcompany.html', {'data': data})
        elif client == '':
            messages.error(request, 'Enter Client company')
            return render(request, 'addParent/addclientcompany.html', {'data': data})
        elif Client.objects.all().filter(country=country).exists() and Client.objects.all().filter(client=client).exists() and Client.objects.all().filter(parent_company=parent_company).exists():
            messages.error(request, 'Client data Already Available')
            return render(request, 'addParent/addclientcompany.html', {'data': data})
        else:
            datas = Parent.objects.get(parent=parent_company)
            # print(datas)
            client_data = Client(parent_company=parent_company, client=client, country=country, parent_data_id=datas.id)

        client_data.save()
        return redirect(parent)

    else:
        return render(request, 'addParent/addclientcompany.html', {'data': data})
