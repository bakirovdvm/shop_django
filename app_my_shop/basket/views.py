from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BasketSerializer, BasketItemSerializer
from .models import Basket, BasktetItem
from product.models import Product
from .serializers import BasketItemSerializer


class BasketView(APIView):
    def get(self, request):
        '''
        Приложение корзины.

        В методе GET мы получаем данные о продукте
        '''

        if request.user.is_authenticated:
            print('USER', request.user)
            queryset = BasktetItem.objects.filter(basket__user=request.user)
            serializer = BasketItemSerializer(instance=queryset, many=True)

            # print('serializer.data'.upper(), serializer.data)
            return Response(serializer.data)

        else:
            session_key = request.session.session_key
            if not session_key:
                request.session.create()
                session_key = request.session.session_key

            queryset = BasktetItem.objects.filter(basket__session_key=session_key)

        print("queryset", queryset)
        serializer = BasketItemSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        '''
        Перейдя на страницу товара, выбираем количество,
        которое хотим купить и нажимаем на кнопку "ADD TO CARD"
        :param request: получаем ID продукта и количество продукта для заказа
        :return:
        '''

        product_id = request.data.get('id')
        quantity = request.data.get('count')
        # print('product_ID', product_id)
        # print('quantity', quantity)

        try:
            product = Product.objects.get(id=product_id)
            # print(product.title, product.price)
        except Product.DoesNotExist:
            return Response({'error': 'product not found'}, status=status.HTTP_404_NOT_FOUND)

        if request.user.is_authenticated:
            basket, created = Basket.objects.get_or_create(user=request.user)
        else:
            session_key = request.session.session_key
            if not session_key:
                request.session.create()
                session_key = request.session.session_key

            basket, created = Basket.objects.get_or_create(session_key=session_key)

        basket_item, created = BasktetItem.objects.get_or_create(basket=basket, product=product)
        basket_item.quantity += int(quantity)
        basket_item.save()
        serializer = BasketItemSerializer(basket_item)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        '''
        Удаление продукта из корзины
        :param request: получаем ID продукта и количество продукта
        :return:
        '''

        product_id = request.data.get('id')
        quantity = request.data.get('count')

        print(product_id, quantity)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'product not found'}, status=status.HTTP_404_NOT_FOUND)

        if request.user.is_authenticated:
            basket, created = Basket.objects.get_or_create(user=request.user)
        else:
            session_key = request.session.session_key
            if not session_key:
                request.session.create()
                session_key = request.session.session_key

            basket, created = Basket.objects.get_or_create(session_key=session_key)

        basket_item, created = BasktetItem.objects.get_or_create(basket=basket, product=product)

        if basket_item.quantity > quantity:
            basket_item.quantity -= int(quantity)

            basket_item.save()
        else:
            basket_item.delete()

        serializer = BasketItemSerializer(basket_item)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
