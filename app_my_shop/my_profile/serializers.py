from rest_framework import serializers

from .models import Avatar, Profile


class AvatarSerializer(serializers.ModelSerializer):
    src = serializers.SerializerMethodField()  # тут возвращаем ссылку на изображение

    class Meta:
        model = Avatar
        fields = ["src", "alt"]

    def get_src(self, obj):
        return obj.src.url


class ProfileSerializer(serializers.ModelSerializer):
    avatar = AvatarSerializer(read_only=True)  # тут берем сериалайзер аватарки

    class Meta:
        model = Profile
        fields = [
            "fullName",
            "email",
            "phone",
            "avatar",
        ]  # тут видим описали только те поля которые мы возвращаем

    def update(self, instance, validated_data):
        avatar_data = validated_data.pop("avatar", None)
        instance = super(ProfileSerializer, self).update(instance, validated_data)

        if avatar_data:
            instance.avatar.update(**avatar_data)

        return instance


class ChangePasswordSerializer(serializers.Serializer):
    currentPassword = serializers.CharField(required=True)
    newPassword = serializers.CharField(required=True)
