from rest_framework import serializers
from .models import Product, Tag, ProductReview, ProductImage, ProductSpecifications, ProductSale


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = '__all__'


class ProductSpecificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSpecifications
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)
    tags = TagSerializer(many=True)
    reviews = ProductReviewSerializer(many=True)
    specifications = ProductSpecificationsSerializer(many=True)
    class Meta:
        model = Product
        fields = '__all__'


class ProductSaleSerializer(serializers.ModelSerializer):
    product = ProductSerializer
    class Meta:
        model = ProductSale
        fields = '__all__'

    dateFrom = serializers.SerializerMethodField
    dateTo = serializers.SerializerMethodField

    def get_dateFrom(self, obj):
        return obj.dateFrom.strftime("%m-%d")

    def get_dateTo(self, obj):
        return obj.dateTo.strftime("%m-%d")
