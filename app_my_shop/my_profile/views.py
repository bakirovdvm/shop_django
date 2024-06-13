from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Profile, Avatar
from .serializers import ProfileSerializer, ChangePasswordSerializer, AvatarSerializer


class ProfileView(APIView):
    '''
    Описывается отображение профиля
    '''
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        profile = Profile.objects.get(user=request.user)  # достаем профиль
        serializer = ProfileSerializer(profile)  # отправляем объект в сериалайзер чтобы привести в формат который ждет фронт
        return Response(serializer.data)  # возвращаем данные

    def post(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordView(APIView):
    '''
    Описывается процедура смены пароля
    '''
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            current_password = serializer.validated_data['currentPassword']
            new_password = serializer.validated_data['newPassword']

            user = request.user

            if user.check_password(current_password):
                user.set_password(new_password)
                user.save()
                return Response({'message': 'Password changed successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Invalid current password"}, status=status.HTTP_400_BAD_REQUEST,)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AvatarView(APIView):
    '''
    описывается процедура смены аватарки
    '''
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        new_avatar = request.FILES.get("avatar")

        if new_avatar:
            user = request.user
            profile = Profile.objects.get(user=user)
            avatar = Avatar.objects.create(src=new_avatar)

            profile.avatar = avatar
            profile.save()

            return Response(
                {"message": "Avatar updated successfully."}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"error": "No file was submitted."}, status=status.HTTP_400_BAD_REQUEST
            )
