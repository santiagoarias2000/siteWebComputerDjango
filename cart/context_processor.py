from .car import Car


def import_total_cart(request):
    car = Car(request)
    total = 0
    if request.user.is_authenticated:
        for key, value in request.session["car"].items():
            total = total + (float(value["price"]) * value["amount"])
    return {"import_total_cart": total}
