from rest_framework import serializers
from .models import Order
from my_profile.models import Profile
from basket.models import BasktetItem
from product.models import ProductReview


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def to_representation(self, instance):
        profile = Profile.objects.get(fullName=instance.fullName)
        products = BasktetItem.objects.filter(basket=instance.basket.pk)

        data = {
            'id': instance.pk,
            'createdAt': instance.createdAt.strftime('%Y.%m.%d %H:%M'),
            'fullName': f'{profile.fullName}',
            'email': profile.email,
            'phone': profile.phone,
            'deliveryType': instance.deliveryType,
            'paymentType': instance.paymentType,
            'status': instance.status,
            'city': instance.city,
            'address': instance.address,
            'products': [
                {
                    "id": item.product.pk,
                    "category": item.product.category.pk,
                    "price": item.product.price,
                    "count": item.quantity,
                    "date": item.product.date.strftime("%Y.%m.%d %H:%M"),
                    "title": item.product.title,
                    "description": item.product.description,
                    "freeDelivery": item.product.freeDelivery,
                    "images": item.product.get_images(),
                    "tags": [
                        {"id": tag.pk, "name": tag.name}
                        for tag in item.product.tags.all()
                    ],
                    "reviews": ProductReview.objects.filter(
                        product_id=item.product.id
                    ).count(),
                    "rating": float(item.product.rating),
                }
                for item in products
            ],

        }

        print('dataaa'.upper(), data)
