from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from products.models import Pc, Products, Pc_character
from products.forms import pc_form, pcs_form


def database_pc(request):
    list_pc = Pc.objects.all()
    return render(request, 'pc/pc_view.html', {'lists': list_pc})


def detail_pc(request, id):
    item = Products.objects.get(id=id)
    item_pc = Pc_character.objects.all().filter(pcs__products__id=id)
    return render(request, 'pc/pc_detail.html', {'item': item, 'item_pc': item_pc})


@permission_required('products.add_pc_character')
def create_pc(request):
    if request.method == 'POST':
        form = pc_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            messages.info(request, 'Save data, go to pc.')
            return render(request, 'pc/pc_create.html', {'form': form, 'img_obj': img_obj})
    else:
        form = pc_form()
    return render(request, 'pc/pc_create.html', {'form': form})


@permission_required('products.add_pc')
def create_pcs(request):
    if request.method == 'POST':
        form_p = pcs_form(request.POST, request.FILES)
        if form_p.is_valid():
            form_p.save()
            img_obj = form_p.instance
            messages.info(request, 'Save data, press the next button.')
            return render(request, 'pc/pcs_create.html', {'form_p': form_p, 'img_obj': img_obj})
    else:
        form_p = pcs_form()
    return render(request, 'pc/pcs_create.html', {'form_p': form_p})


@permission_required('products.change_pc_character')
def update_pc(request, id):
    pc = Pc_character.objects.get(pcs__products_id=id)
    update_form = pc_form(request.POST or None, instance=pc)
    if update_form.is_valid():
        update_form.save()
        messages.info(request, 'update data to the pc.')
        return redirect('/products/update/pc/'+id)
    name_pc = Pc.objects.get(products_id=id)

    context = {
        'update_form': update_form,
        'name': name_pc
    }
    return render(request, 'pc/pc_update.html', context)


@permission_required('products.delete_pc')
def delete_pc(request, id):
    pc_get = Pc.objects.get(id=id)
    if request.method == 'POST':
        pc_get.delete()
        messages.info(request, 'Delete data on the database.')
        return redirect('view_pc')
    return render(request, {'pc': pc_get})
