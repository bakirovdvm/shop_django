from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import CategorySerializer, SubCategorySerializer
from .models import Category, Subcategory


class CategoriesView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        category_data = list()
        for category in categories:
            print('pk'.upper(), category.pk)
            print('category'.upper(), category.title)
            print('image'.upper(), category.get_image())


            subcategories = Subcategory.objects.all()
            for subcategory in subcategories:
                print('pk'.upper(), subcategory.pk)
                print('category'.upper(), subcategory.title)
                print('image'.upper(), subcategory.get_image())
