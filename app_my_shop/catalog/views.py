from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import CategorySerializer, SubCategorySerializer
from .models import Category, Subcategory


class CategoriesView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        category_result_list = list()

        for category in categories:
            # subcategories = category.subcategory.all()
            subcategories = Subcategory.objects.filter(category=category)
            subcategories_list = list()
            for subcategory in subcategories:
                subcategories_dict = {
                    'id': subcategory.pk,
                    'title': subcategory.title,
                    'image': subcategory.get_image()
                }

                subcategories_list.append(subcategories_dict)

            category_dict = {
                'id': category.pk,
                'title': category.title,
                'image': category.get_image(),
                'subcategories': subcategories_list
            }
            print('category_dict'.upper(), category_dict)
            category_result_list.append(category_dict)

        print('category_result_list'.upper(), category_result_list)

        return JsonResponse(category_result_list, safe=False)


