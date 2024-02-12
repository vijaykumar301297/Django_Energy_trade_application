from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_control
from django.shortcuts import render, redirect
from .models import Parent, Client


# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def addcompany(request):
    return render(request, 'addParent/addParent.html', {'navbar': 'createcompany'})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def parent(request):
    data = Parent.objects.all()
    # datas = Client.objects.all().count()
    p = Paginator(data, 7)
    page = request.GET.get("page")
    datas = p.get_page(page)
    
    return render(request, 'addParent/parent.html', {'data': data, 'navbar': 'parent', 'datas': datas })


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
        return redirect(addcompany)
    
    else:
        return render(request, 'addParent/addparentcompany.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def client(request):
    data = Client.objects.all()
    p = Paginator(data, 7)
    page = request.GET.get("page")
    datas = p.get_page(page)
    return render(request, 'addParent/client.html', {'data': data, 'navbar': 'client', 'datas': datas, 'nav':'client'})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def addclientcompany(request):
    data = Parent.objects.all()
    
    if request.method == 'POST':
        parent_company = request.POST['parent_company']
        client = request.POST['client']
        country = request.POST['country']
        # parent_company = request.POST['parent_company']
        datas = Parent.objects.get(id=parent_company)
        if parent_company == '':
            messages.error(request, 'Enter Parent company')
            return render(request, 'addParent/addclientcompany.html', {'data': data})
        
        elif client == '':
            messages.error(request, 'Enter Client company')
            return render(request, 'addParent/addclientcompany.html', {'data': data})
        
        elif Client.objects.all().filter(country=country, client=client, parent_data_id=parent_company):
            
            messages.error(request, 'Client data Already Available')
            return render(request, 'addParent/addclientcompany.html', {'data': data, 'd': d, 'c': c, 'p': p})
        
        else:
            
            client_data = Client(client=client, country=country, parent_data_id=datas.id, state='Active')
        
        client_data.save()
        return redirect(parent)
    
    else:
        return render(request, 'addParent/addclientcompany.html', {'data': data})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def edit_parent(request, id):
    parent_data = Parent.objects.get(pk=id)
    context = {
        'parent_data': parent_data
    }
    if request.method == 'POST':
        parent_data.parent = request.POST['parent']
        parent_data.save()
        
        return redirect(addcompany)
    
    return render(request, 'addParent/edit_parent.html', context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def edit_client(request, id):
    client_data = Client.objects.get(pk=id)
    parent_data = Parent.objects.all()
    context = {
        'client_data': client_data,
        'parent_data': parent_data
    }
    if request.method == 'POST':
        client_data.parent_data_id = request.POST['parent_company']
        client_data.client = request.POST['client']
        client_data.country = request.POST['country']
        
        client_data.save()
        return redirect(parent)
    
    return render(request, 'addParent/edit_client.html', context)
