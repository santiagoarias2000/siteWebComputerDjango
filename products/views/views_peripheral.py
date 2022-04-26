from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from products.models import Peripheral, Products, Type_peripheral
from products.forms import peripheral_form, type_per_form


def database_type(request):
    list_t = Type_peripheral.objects.all()
    list_type = Peripheral.objects.all()
    data = {''
            'lists': list_type,
            'type': list_t
            }
    return render(request, 'peripheral/peripheral_view.html', data)


def detail_peripheral(request, id):
    item = Products.objects.get(id=id)
    item_peripheral = Peripheral.objects.all().filter(products_id=id)
    return render(request, 'peripheral/peripheral_detail.html', {'item': item, 'item_peripheral': item_peripheral})


@permission_required('products.add_peripheral')
def create_peripheral(request):
    if request.method == 'POST':
        form = peripheral_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            messages.info(request, 'Save data a peripheral in database')
            return render(request, 'peripheral/peripheral_create.html', {'form': form, 'img_obj': img_obj})
    else:
        form = peripheral_form()
    return render(request, 'peripheral/peripheral_create.html', {'form': form})


@permission_required('products.change_peripheral')
def update_peripheral(request, id):
    peripheral = Peripheral.objects.get(products_id=id)
    update_form = peripheral_form(request.POST or None, instance=peripheral)
    if update_form.is_valid():
        update_form.save()
        messages.info(request, 'Update '+peripheral.products.name+' in the database.')
        return redirect('/products/update/peripheral/'+id)
    name_product = Peripheral.objects.get(products_id=id)
    context = {
        'update_form': update_form,
        'name': name_product
    }

    return render(request, 'peripheral/peripheral_update.html', context)


@permission_required('products.delete_peripheral')
def delete_peripheral(request, id):
    peripheral_get = Peripheral.objects.get(id=id)
    if request.method == 'POST':
        peripheral_get.delete()
        messages.info(request, 'Delete element in the data base')
        return redirect('view_type-peripheral')
    return render(request, {'peripheral': peripheral_get})


def data_typeperipheral(request, id):
    list_t = Type_peripheral.objects.all()
    list_type = Peripheral.objects.all().filter(type_peripherals__id=id)
    data = {
        'lists': list_type,
        'type': list_t
    }
    return render(request, 'peripheral/keyboard_list.html', data)
