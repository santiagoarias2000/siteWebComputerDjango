from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from products.forms import laptop_form, laptops_form
from products.models import Laptop, Products, Laptops_character
from django.contrib import messages


def database_laptop(request):
    products_list = Laptop.objects.all()
    return render(request, 'laptop/view_laptop.html', {'lists': products_list})


def detail_laptop(request, id):
    item = Products.objects.get(id=id)
    item_l = Laptops_character.objects.all().filter(laptops__products_id=id)
    return render(request, 'laptop/laptop_detail.html', {'item': item, 'item_l': item_l})


@permission_required('products.add_laptops_character')
def create_laptop(request):
    if request.method == 'POST':
        form = laptop_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            data_save = {
                'form': form,
                'img_obj': img_obj,
            }
            messages.info(request, 'Save data, go to laptop.')
            return render(request, 'laptop/laptop_create.html', data_save)
    else:
        form = laptop_form()
    return render(request, 'laptop/laptop_create.html', {'form': form})


@permission_required('products.add_laptop')
def create_laptops(request):
    if request.method == 'POST':
        form_l = laptops_form(request.POST, request.FILES)
        if form_l.is_valid():
            form_l.save()
            img_obj = form_l.instance
            messages.info(request, 'Save data, press the next button.')
            data_save = {
                'img_obj': img_obj,
                'form_l': form_l
            }
            return render(request, 'laptop/laptops_create.html', data_save)
    else:
        form_l = laptops_form()
    return render(request, 'laptop/laptops_create.html', {'form_l': form_l})


@permission_required('products.add_laptop_character')
def update_laptop(request, id):
    laptop = Laptops_character.objects.get(laptops__products_id=id)
    update_form = laptop_form(request.POST or None, instance=laptop)
    if update_form.is_valid():
        update_form.save()
        messages.info(request, 'Update laptop in the database.')
        return redirect('/products/update/laptop/' + id)
    name_product = Laptop.objects.get(products_id=id)
    context = {
        'update_form': update_form,
        'name': name_product
    }
    return render(request, 'laptop/laptop_update.html', context)


@permission_required('products.delete_laptop')
def delete_laptop(request, id):
    laptop_get = Laptop.objects.get(id=id)
    if request.method == 'POST':
        laptop_get.delete()
        messages.info(request, 'Data delete on the database.')
        return redirect('view_laptops')
    return render(request, {'laptop': laptop_get})
