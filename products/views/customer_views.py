from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from products.forms import customer_form, superuser_form
from products.models import Customer, User


def create_user(request):
    data = {
        'form': customer_form
    }
    if request.method == 'POST':
        form_user = customer_form(data=request.POST)
        if form_user.is_valid():
            form_user.save()
            messages.info(request, 'User create in the system.')
            user = authenticate(username=form_user.cleaned_data["username"],
                                password=form_user.cleaned_data['password1'])
            login(request, user)
            return redirect('index')
        data
    return render(request, 'user_customer/user_create.html', data)


@permission_required('products.add_products')
def create_superuser(request):
    data = {
        'form': superuser_form
    }
    if request.method == 'POST':
        form_user = superuser_form(data=request.POST)
        if form_user.is_valid():
            form_user.save()
            user = authenticate(username=form_user.cleaned_data["username"],
                                password=form_user.cleaned_data['password1'])
            login(request, user)
            return redirect('index')
        data
    return render(request, 'user_customer/superuser_create.html', data)


def login_view(request):
    if request.method == 'POST':
        _username = request.POST['username']
        _password = request.POST['password']
        user = authenticate(request, username=_username, password=_password)
        print(user)
        if user:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'user_customer/login.html', {'error': 'User do not register in database'})

    return render(request, 'user_customer/login.html')


@login_required
def logout_v(request):
    logout(request)
    return redirect('index')


def views_user(request):
    list_user = User.objects.all()
    return render(request, 'user_customer/user_view.html', {'list': list_user})


@permission_required('products.delete_products')
def delete_user(request, id):
    user_get = User.objects.get(id=id)
    if request.method == 'POST':
        user_get.delete()
        messages.info(request, 'Delete user in the system.')
        return redirect('views_user')
    return render(request, {'user': user_get})
