from django.db import models
from basket.models import Basket
from product.models import Product


class Order(models.Model):
    PAYMENT = (
        ('online', 'Онлайн картой'),
        ('оффлайн', 'Онлайн с чужой карты')
    )
    DELIVERY = (
        ('delivery_free', 'Обычная бесплатная доставка'),
        ('pickup', 'Экспресс доставка')
    )

    createdAt = models.DateTimeField(auto_now_add=True)
    fullName = models.CharField(max_length=80)
    email = models.EmailField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)

    deliveryType = models.CharField(max_length=80, choices=DELIVERY, default='Обычная доставка')
    paymentType = models.CharField(max_length=30, choices=PAYMENT, default='Онлайн картой')

    totalCost = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    status = models.CharField(max_length=200, default='in process')

    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='orders', default=None)
    city = models.CharField(max_length=120, null=True, blank=True)
    address = models.CharField(max_length=120, null=True, blank=True)
    products = models.ManyToManyField(Product, related_name='orders')

