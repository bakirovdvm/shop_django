from rest_framework import serializers
from .models import Basket, BasktetItem
from product.serializers import ProductSerializer


class BasketItemSerializer(serializers.Serializer):
    class Meta:
        model = BasktetItem
        fields = 'product', 'quantity'

    def to_representation(self, instance):
        data = ProductSerializer(instance.product).data
        data['count'] = instance.quantity
        print(data)
        return data


class BasketSerializer(serializers.Serializer):
    items = BasketItemSerializer(many=True)

    class Meta:
        model = Basket
        fields = '__all__'
