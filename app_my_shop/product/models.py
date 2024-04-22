from django.db import models
from catalog.models import Subcategory


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='subCategoryProduct')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    count = models.IntegerField(default=100)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    fullDescription = models.TextField()
    freeDelivery = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=3, default=0, decimal_places=2)
    tags = models.ManyToManyField(Tag, related_name='tags')

    def __str__(self):
        return self.title

    def get_images(self):
        images = ProductImage.objects.filter(product_id=self.pk)
        return [{"src": image.src.url, "alt": image.src.name} for image in images]

    def get_tags(self):
        tags = Tag.objects.filter(product_id=self.pk)
        return [tag.name for tag in tags]

    def get_reviews(self):
        reviews = ProductReview
        return [review.text for review in reviews]


def product_images_directory_path(instance: 'ProductImage', filename: str) -> str:
    return 'products/product_{pk}'.format(
        pk=instance.product.pk,
        filename=filename
    )


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    src = models.ImageField(upload_to=product_images_directory_path)
    alt = models.CharField(max_length=200, null=False, blank=True, default='image')

    def __str__(self):
        return self.alt


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    author = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    text = models.TextField()
    rate = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)


class ProductSpecifications(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='specifications')
    name = models.CharField(max_length=200)
    value = models.TextField()
