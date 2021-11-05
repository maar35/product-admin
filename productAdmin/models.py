from datetime import date, time
from django.db import models


# Product model.
class Product(models.Model):
    name = models.CharField(max_length=32, unique=True, default="no-product")
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=16, decimal_places=2, default=999999.99)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return ", ".join([
            self.name,
            self.description,
            str(self.price),
            str(self.stock)
        ])


# Order model.
class Order(models.Model):
    order_date = models.DateField('order entry date', auto_now_add=True)
    order_time = models.TimeField('order entry time', auto_now_add=True)
    customer_name = models.CharField(max_length=72, )
    shipping_address = models.CharField(max_length=300)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return ", ".join([
            " ".join([
                self.order_date.isoformat(),
                self.order_time.isoformat(timespec='minutes')
            ]),
            self.product.name,
            self.customer_name
        ])
