from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BasketSerializer, BasketItemSerializer
from .models import Basket, BasktetItem
from product.models import Product


class BasketView(APIView):
    def get(self, request):
        print('OLLLA', request)
        print('OLLLA', request.data)
        if request.user.is_authenticated:
            print('USER', request.user)
            queryset = BasktetItem.objects.filter(basket__user=request.user)
            serializer = BasketItemSerializer(instance=queryset, many=True)

            print('serializer.data'.upper(), serializer.data)
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
        product_id = request.data.get('id')
        quantity = request.data.get('count')
        print('product_ID', product_id)
        print('quantity', quantity)

        try:
            product = Product.objects.get(id=product_id)
            print(product.title, product.price)
        except Product.DoesNotExist:
            return Response({'error': 'product not found'}, status=status.HTTP_404_NOT_FOUND)

