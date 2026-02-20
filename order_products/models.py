from django.db import models
from orders.models import Order


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              related_name="order_products")
    name = models.CharField(max_length=127)
    amount = models.PositiveIntegerField()
    shop_id = models.CharField(max_length=127)

    def __str__(self):
        return f"{self.name} (x{self.amount}) — Order #{self.order_id}"
