from rest_framework import serializers
from .models import Order
from my_profile.models import Profile
from basket.models import BasktetItem


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def to_representation(self, instance):
        profile = Profile.objects.get(fullName=instance.fullName)
        products = BasktetItem.objects.filter(basket=instance.basket.pk)

        data = {
            'id': instance.pk,
            'createdAt': instance.createdAt.strftime('%Y.%m.%d %H:%M')
        }

        print('data'.upper(), data)
