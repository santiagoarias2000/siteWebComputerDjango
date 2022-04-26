from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

    class Meta:
        db_table = 'customer'


class Bill(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    data_buy = models.DateTimeField()

    def __str__(self):
        return str(self.id)

    def bill_id(self):
        return 'Bill' + str(self.id)

    def get_cost_total(self):
        return sum(item.get_cost() for item in self.items.all())

    class Meta:
        db_table = 'bill'


class Products(models.Model):
    name = models.CharField(max_length=50)
    description_general = models.CharField(max_length=400)
    image = models.ImageField(upload_to='resouce')
    price = models.IntegerField('Price')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'


class Detail(models.Model):
    amount = models.IntegerField(default=1)
    product_id = models.ForeignKey(Products, related_name='items_order', on_delete=models.CASCADE)
    bill_id = models.ForeignKey(Bill, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField('Price')

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.amount

    class Meta:
        db_table = 'detail'


class Laptop(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return self.products.name

    class Meta:
        db_table = 'laptop'


class Laptops_character(models.Model):
    laptops = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    graphic_card = models.CharField(max_length=100)
    keyboard = models.CharField(max_length=100)
    display = models.CharField(max_length=100)
    processor = models.CharField(max_length=50)
    memory = models.CharField(max_length=50)
    storage = models.CharField(max_length=50)
    warranty = models.CharField(max_length=100)

    def __str__(self):
        return self.laptops.products.name

    class Meta:
        db_table = 'laptops_character'


class Type_peripheral(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'type_peripheral'


class Peripheral(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    type_peripherals = models.ForeignKey(Type_peripheral, on_delete=models.CASCADE)
    description = models.CharField(max_length=400)
    link_website = models.CharField(max_length=300)

    def __str__(self):
        return self.products.name

    class Meta:
        db_table = 'peripheral'


class Monitor(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return self.products.name

    class Meta:
        db_table = 'monitor'


class Monitor_character(models.Model):
    monitors = models.ForeignKey(Monitor, on_delete=models.CASCADE)
    size = models.CharField(max_length=100)
    hz = models.CharField(max_length=100)
    quality = models.CharField(max_length=100)

    def __str__(self):
        return self.monitors.products.name

    class Meta:
        db_table = 'monitor_character'


class Pc(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return self.products.name

    class Meta:
        db_table = 'pc'


class Pc_character(models.Model):
    pcs = models.ForeignKey(Pc, on_delete=models.CASCADE)
    peripherals = models.ForeignKey(Peripheral, on_delete=models.CASCADE)
    graphic_card = models.CharField(max_length=100)
    board = models.CharField(max_length=100)
    monitors = models.ForeignKey(Monitor, on_delete=models.CASCADE)
    processor = models.CharField(max_length=50)
    memory = models.CharField(max_length=50)
    storage = models.CharField(max_length=50)
    refrigeration = models.CharField(max_length=100)

    def __str__(self):
        return self.pcs.products.name

    class Meta:
        db_table = 'pc_character'
