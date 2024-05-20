from django.shortcuts import render
from rest_framework.views import APIView


class BasketView(APIView):
    def post(self, request):
        print('OLLLA', request)
        print('OLLLA', request.data)
