from django.db import models
from order.models import Order


class Payment(models.Model):
    '''
    Описывается модель онлайн оплаты.

    Имеются поля с данными платжной карточки (номер, имя, дата истечения и тд)
    '''

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payment_order')
    card_number = models.IntegerField()
    card_name = models.CharField(max_length=80)
    card_month = models.CharField(max_length=3)
    card_year = models.CharField(max_length=3)
    card_cvv_code = models.CharField(max_length=3)
    payment_status = models.BooleanField(default=False)
