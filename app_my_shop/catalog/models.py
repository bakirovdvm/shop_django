from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200, default='CategoryName')

    def __str__(self):
        return self.title

    def get_image(self):
        images = CategoryImage.objects.filter(category_id=self.pk)
        images_data = dict()
        for i in images:
            images_data = {'src': i.src.url, 'alt': i.src.name}
        return images_data


class Subcategory(models.Model):
    title = models.CharField(max_length=200, default='SubCategoryName')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategory')

    def __str__(self):
        return self.title

    def get_image(self):
        images = SubCategoryImage.objects.filter(subcategory_id=self.pk)
        images_data = dict()
        for i in images:
            images_data = {'src': i.src.url, 'alt': i.src.name}
        return images_data


class CategoryImage(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='images')
    src = models.ImageField(upload_to='category/items/')
    alt = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.src.name


class SubCategoryImage(models.Model):
    category = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='images')
    src = models.ImageField(upload_to='subcategory/items/')
    alt = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.src.name
