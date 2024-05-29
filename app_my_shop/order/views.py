from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import OrderSerializer
from .models import Order


class OrderView(APIView):
    # def get(self, request):
    #     print(request)
    #     print(request.data)

    def post(self, request):
        print(request)
        # print(request.data)



class OrderDetail(APIView):
    def get(self, request, order_id):
        order = Order.objects.get(pk=order_id)
        serializer = OrderSerializer(order)
        print(serializer.data)

