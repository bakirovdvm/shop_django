import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from my_profile.models import Profile


class SignInView(APIView):
    def post(self, request):
        '''
        Описывается процедура аутентификации пользователя
        :param request:
        :return:
        '''
        serialized_data = list(request.POST.keys())[0]
        user_data = json.loads(serialized_data)
        username = user_data.get("username")
        password = user_data.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SignUpView(APIView):  # наследуемся от APIView(выше кидал документацию на него)
    '''
    Описывается процесс регистрации нового пользователя,
    с учетом его пустой или набранной корзины
    '''
    def post(self, request):  # (рас у в контракте только post запрос описываем только его)

        serialized_data = list(request.data.keys())[0]
        user_data = json.loads(serialized_data)
        name = user_data.get("name")
        username = user_data.get("username")
        password = user_data.get("password")

        # try:
        user = User.objects.create_user(username=username, password=password)
        profile = Profile.objects.create(user=user, fullName=name)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_201_CREATED)

        else:
            # except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def signOut(request):
    logout(request)
    return HttpResponse(status=200)
