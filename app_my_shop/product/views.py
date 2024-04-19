from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductSerializer
from .models import Product



class ProductView(APIView):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(pk=product_id)
            serialiaer = ProductSerializer(product)
            print(serialiaer.data)
            return Response(serialiaer.data)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        # print(request)
        # print(request.data)
        # print(product_id)
        # print(request.user)


