from django.shortcuts import render
from rest_framework.views import APIView
from order.models import Order
import datetime
from django.http import JsonResponse, HttpResponse
from .models import Payment
from basket.models import Basket, BasktetItem
from product.models import Product


class PaymentView(APIView):
    '''
    Описывается процедура онлайн оплаты заказа,
    и затем опустошение корзины после успешной оплаты
    '''

    def post(self, request, id):
        print(request.data)
        order = Order.objects.get(id=id)

        data = request.data

        card_number = data['number']
        card_name = data['name']
        card_month = data['month']
        card_year = data['year']
        card_code = data['code']

        current_month = datetime.datetime.now().month
        current_year = datetime.datetime.now().year % 100
        # print('current_year', current_year)
        # print('current_month', current_month)

        if int(card_year) < current_year or (
                int(card_year) == current_year and int(card_month) < current_month
        ):
            order = Order.objects.get(id=id)
            order.status = "card expired"
            order.save()
            return JsonResponse({"error": "card expired"}, status=500)

        if len(card_number) != 16 or int(card_month) > 12:
            return JsonResponse({"error": "card invalid"}, status=400)

        order = Order.objects.get(id=id)
        order.status = "successful"
        order.save()
        payment = Payment.objects.create(
            order=order,
            card_name=card_name,
            card_number=card_number,
            card_year=card_year,
            card_month=card_month,
            card_cvv_code=card_code,
        )

        basket = Basket.objects.get(user=request.user)
        basket_item = BasktetItem.objects.filter(basket=basket)

        for item in basket_item:
            product = Product.objects.get(pk=item.product.id)

            if product.count < item.quantity:
                print("Недостаточно продукта на складе")
                return JsonResponse({"error": "Недостаточно продукта на складе"})
            product.count -= item.quantity
            product.save()
            payment.status = True
            payment.save()

        basket_item.delete()

        return HttpResponse(status=200)

