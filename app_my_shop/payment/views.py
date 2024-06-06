from django.shortcuts import render
from rest_framework.views import APIView


class PaymentView(APIView):
    def post(self, request):
        print('requestPAYMENT', request)
        print(request.data)
