from django.shortcuts import redirect, get_object_or_404, render
from cart.car import Car
from products.models import Products
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


def add_product(request, product_id):
    car = Car(request)
    product = get_object_or_404(Products, id=product_id)
    car.add(product=product)
    return redirect('view_car')


def delete_product(request, product_id):
    car = Car(request)
    product = Products.objects.get(id=product_id)
    car.delete(product=product)
    return redirect('view_car')


def subtract_product(request, product_id):
    car = Car(request)
    product = Products.objects.get(id=product_id)
    car.subtract_product(product=product)
    return redirect('view_car')


def clean_car(request):
    car = Car(request)
    car.clean_car()
    return redirect('view_car')


def send_mail(mail):
    context = {'mail': mail}
    template = get_template(('car/information.html'))
    content = template.render(context)
    is_email = EmailMultiAlternatives(
        'Your buys this confirm.',
        'holaaaaa',
        settings.EMAIL_HOST_USER,
        [mail],
    )
    is_email.attach_alternative(content, 'text/html')
    is_email.send()


def email(request):
    if request.method == 'POST':
        mail = request.POST.get('mail')
        send_mail(mail)
    return render(request, 'car/car_view.html')
