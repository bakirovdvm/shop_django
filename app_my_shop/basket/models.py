from django.db import models
from product.models import Product
from django.contrib.auth.models import User


class Basket(models.Model):
    '''
    Модель корзины, в которую будем складывать единицы товаров/продутков.

    Имеется поле Пользователя, которая связана с User'ом,
    Ключ сессии для сбора корзины неавторизованных пользователей,
    так же автоматическая дата создания корзины
    '''

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    session_key = models.CharField(max_length=80, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'basket {self.id}'


class BasktetItem(models.Model):
    '''
    Модель единицы товара/продукта, которая помещается в корзину.

    Имеются поле: Продукта, который связан с моделью продукта,
    Корзины, который связан с моделью продукта,
    количества и автоматическая дата создания единицы
    '''

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product.title}'



