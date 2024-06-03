from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import OrderSerializer
from .models import Order
from my_profile.models import Profile
from basket.models import Basket, BasktetItem


class OrderView(APIView):
    # def get(self, request):
    #     print(request)
    #     print(request.data)

    def post(self, request):
        print(request)
        try:
            print()
            print()
            print(request.user)
            if request.user.is_authenticated:
                profile = Profile.objects.get(user=request.user)
                basket = Basket.objects.get(user=request.user)
                print('basket', basket)
                print('basket', profile.fullName)
            else:
                session_key = request.session.session_key
                if not session_key:
                    request.session.create()
                    session_key = request.session.session_key

                basket = Basket.objects.get(session_key=session_key)
                print('basket_free_user', basket)
                order = Order.objects.create(basket=basket)
                print('order_basket_free_user', order)
                order.save()

                response_data = {"orderId": order.pk}
                print("response_data", response_data)
                return JsonResponse(response_data)

            basket_items = BasktetItem.objects.filter(basket=basket)
            order = Order.objects.create(fullName=profile.fullName, basket=basket)

            for item in basket_items:
                print(item, "=", end=" ")
                print(item.quantity)
                print()

        except Basket.DoesNotExist:
            error_data = {"error": "У пользователя еще нет корзины"}

        order.save()

        response_data = {"orderId": order.pk}
        return JsonResponse(response_data)



class OrderDetailView(APIView):
    def get(self, request, order_id):
        try:
            order = Order.objects.get(pk=order_id)
        except Order.DoesNotExist:
            return JsonResponse({'error': 'Order not found'}, status=404)

        try:
            profile = Profile.objects.get(fullName=order.fullName)
        except profile.DoesNotExist:
            session_key = request.session.session_key
            print('session_key'.upper(), session_key)

            response_data = {'orderId': order.id}

            return Response(response_data, status=200)

        serializer = OrderSerializer(order)
        # print('SERIALIZER GET ORDER', serializer.data)

        return JsonResponse(serializer.data)



