from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    # category
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


def product_images_directory_path(instance: 'ProductImage', filename: str) -> str:
    return 'products/product_{pk}'.format(
        pk=instance.product.pk,
        filename=filename
    )


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    src = models.ImageField(upload_to=product_images_directory_path)
    alt = models.CharField(max_length=200)

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
