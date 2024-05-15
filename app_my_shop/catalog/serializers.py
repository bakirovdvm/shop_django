from rest_framework import serializers
from product.models import Product, ProductReview, Tag


class ProductsPopularSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        review = ProductReview.objects.filter(product_id=instance.id).values_list(
            "rate", flat=True
        )
        tags = Tag.objects.filter(tags__id=instance.id)

        if review.count() == 0:
            rating = "Отзывов пока нету"
        else:
            rating = sum(review) / review.count()

        representation["id"] = instance.id
        representation["category"] = instance.category.pk
        representation["title"] = instance.title
        representation["count"] = instance.count
        representation["description"] = instance.description
        representation["freeDelivery"] = instance.freeDelivery
        representation["date"] = instance.date
        representation["price"] = instance.price
        representation["images"] = instance.get_images()
        representation["tags"] = [{"id": tag.pk, "name": tag.name} for tag in tags]
        representation["reviews"] = review.count()
        representation["rating"] = rating

        return representation


class BannerSerializer(ProductsPopularSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        tags = Tag.objects.filter(tags__id=instance.id)
        representation["tags"] = [tag.name for tag in tags]
        representation["id"] = instance.id
        representation["category"] = instance.category.pk

        return representation


class CatalogSerizlizer(ProductsPopularSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        tags = Tag.objects.filter(tags__id=instance.id)
        representation["tags"] = [tag.name for tag in tags]
        representation["id"] = instance.id
        representation["category"] = instance.category.pk
        # print('instance.currentPage', instance.currentPage)

        return representation
