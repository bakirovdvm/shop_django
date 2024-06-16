from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductSerializer, ProductReviewSerializer
from .models import Product



class ProductView(APIView):
    '''
    Описывается отображение продукта на странице
    '''

    def get(self, request, product_id):
        try:
            product = Product.objects.get(pk=product_id)
            serialiaer = ProductSerializer(product)
            # print(serialiaer.data)
            # serialiaer.data['category'] = 1
            # print(serialiaer.data)
            return Response(serialiaer.data)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)


class ProductReview(APIView):
    '''
    Описывается отображение и добавление отзыва к продукту
    '''

    def get(self, request, id):
        reviews = ProductReview.objects.filter(pk=id)
        serializer = ProductReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request, id):
        product = get_object_or_404(Product, pk=id)
        request.data['product'] = id
        serializer = ProductReviewSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
