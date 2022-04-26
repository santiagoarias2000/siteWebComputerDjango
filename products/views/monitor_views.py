from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from products.models import Monitor, Products, Monitor_character
from products.forms import monitor_form, monitors_form


def database_monitor(request):
    list_monitors = Monitor.objects.all()
    return render(request, 'monitor/monitors_view.html', {'lists': list_monitors})


def detail_monitor(request, id):
    item = Products.objects.get(id=id)
    item_monitor = Monitor_character.objects.all().filter(monitors__products_id=id)
    return render(request, 'monitor/monitor_detail.html', {'item': item, 'item_monitor': item_monitor})


@permission_required('products.add_monitor_character')
def create_monitor(request):
    if request.method == 'POST':
        form = monitor_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            data_save = {
                'form': form,
                'img_obj': img_obj
            }
            messages.info(request, 'create monitor in the database.')
            return render(request, 'monitor/monitor_create.html', data_save)
    else:
        form = monitor_form
    return render(request, 'monitor/monitor_create.html', {'form': form})


@permission_required('products.add_monitor')
def create_monitors(request):
    if request.method == 'POST':
        form_l = monitors_form(request.POST, request.FILES)
        if form_l.is_valid():
            form_l.save()
            img_obj = form_l.instance
            messages.info(request, 'Save data, press the next button.')
            return render(request, 'monitor/monitors_create.html', {'form_l': form_l, 'img_obj': img_obj})
    else:
        form_l = monitors_form()
    return render(request, 'monitor/monitors_create.html', {'form_l': form_l})


@permission_required('products.change_monitor_character')
def update_monitor(request, id):
    monitor = Monitor_character.objects.get(monitors__products_id=id)
    update_form = monitor_form(request.POST or None, instance=monitor)
    if update_form.is_valid():
        update_form.save()
        messages.info(request, 'Update to the monitor in the database.')
        return redirect('/products/update/monitor/'+id)

    name_product = Monitor.objects.get(products_id=id)
    context = {
        'update_form': update_form,
        'name': name_product
    }
    return render(request, 'monitor/monitor_update.html', context)


@permission_required('products.delete_monitor')
def delete_monitor(request, id):
    monitor_get = Monitor.objects.get(id=id)
    if request.method == 'POST':
        monitor_get.delete()
        messages.info(request, 'Data delete on the database.')
        return redirect('view_monitors')
    return render(request, {'monitor': monitor_get})
