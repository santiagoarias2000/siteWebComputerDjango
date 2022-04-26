from django.shortcuts import render


def views(request):
    return render(request, 'user_customer/index.html')


def cart(request):
    return render(request, 'car/car_view.html')