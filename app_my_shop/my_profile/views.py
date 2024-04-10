from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Profile
from .serializers import ProfileSerializer


class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        print('!!!!!!!!!!!')
        print('1', request.user)
        print('2', request.data)
        profile = Profile.objects.get(user=request.user)  # достаем профиль
        print('1111111111111')
        serializer = ProfileSerializer(profile)  # отправляем объект в сериалайзер чтобы привести в формат который ждет фронт

        return Response(serializer.data)  # возвращаем данные

