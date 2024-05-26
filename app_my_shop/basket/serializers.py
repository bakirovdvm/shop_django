from rest_framework import serializers
from .models import Basket, BasktetItem
from product.serializers import ProductSerializer


class BasketItemSerializer(serializers.Serializer):
    class Meta:
        model = BasktetItem
        fields = '__all__'

    def to_representation(self, instance):
        print('instance'.upper(), instance)
        print('instance.product'.upper(), instance.product)
        data = ProductSerializer(instance.product).data
        data['count'] = instance.quantity
        # print('data-basketitemserializer'.upper(), data)
        return data


class BasketSerializer(serializers.Serializer):
    items = BasketItemSerializer(many=True)

    class Meta:
        model = Basket
        fields = '__all__'
