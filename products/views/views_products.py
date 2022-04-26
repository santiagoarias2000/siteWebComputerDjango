from django.contrib import messages
from django.shortcuts import render, redirect
from products.models import Products
from products.forms import product_form
from django.contrib.auth.decorators import login_required, permission_required


def database_views(request):
    products_list = Products.objects.all()
    return render(request, 'products/products_view.html', {'lists': products_list})


@permission_required('products.add_products')
def create_data(request):
    if request.method == 'POST':
        form = product_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            obj_img = form.instance
            messages.info(request, 'Save data in a product in database')
            return render(request, 'products/product_create.html', {'form': form, 'obj_img': obj_img})
    else:
        form = product_form()
    return render(request, 'products/product_create.html', {'form': form})


@permission_required('products.delete_products')
def delete_data(request, id):
    product_get = Products.objects.get(id=id)
    if request.method == 'POST':
        product_get.delete()
        messages.info(request, 'Delete product on the database.')
        return redirect('view_products')
    return render(request, {'product': product_get})


def filter_one_product(request):
    name_search = request.POST.get('name_product', False)
    filter_product = Products.objects.filter(name=name_search)
    messages.info(request, 'this product')
    return render(request, 'products/product_filter.html', {'filter_product': filter_product})
