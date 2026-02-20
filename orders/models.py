from django.db import models
from django.conf import settings


class Order(models.Model):
    class Payment(models.TextChoices):
        PIX = "Pix", "Pix"
        CARTAO = "Cartão", "Cartão"
        BOLETO = "Boleto", "Boleto"

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name="orders")
    name = models.CharField(max_length=127)
    email = models.EmailField(max_length=127)
    address = models.TextField()
    payment = models.CharField(max_length=10, choices=Payment.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.pk} - {self.user}"
