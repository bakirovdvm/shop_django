from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CategorySerializer, SubCategorySerializer, ProductSerializer
from .models import Category, Subcategory
from product.models import Product
from rest_framework.generics import ListAPIView
from .serializers import BannerSerializer, ProductsPopularSerializer


class CategoriesView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        category_result_list = list()

        for category in categories:
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
            # print('category_dict'.upper(), category_dict)
            category_result_list.append(category_dict)

        # print('category_result_list'.upper(), category_result_list)

        return JsonResponse(category_result_list, safe=False)


class CatalogView(APIView):
    def get(self, request):
        product = Product.objects
        serializer = ProductSerializer(product.distinct(), many=True)

        filter_name = request.query_params.get('filter[name]')
        mminpice = request.query_params.get('filter[minPrice]')
        maxPrice = request.query_params.get('filter[maxPrice]')
        free_delivery = request.query_params.get('filter[freedelivery]')
        available = request.query_params.get("filter[available]", True)
        tags = request.query_params.getlist("tags[]")


        # print('items'.upper(), serializer.data)
        request_data = {
            'items': serializer.data,
            'currentPage': request.query_params.get('currentPage'),
            'lastPage': request.query_params.get('lastPage')
        }

        return Response(request_data)


class ProductsPopularView(ListAPIView):
    serializer_class = BannerSerializer
    def get_queryset(self):
        return Product.objects.filter(count__gt=0)[:1]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ProductsLimitedView(ListAPIView):
    '''
    Описывается отображение товаров/продуктов на главной странице сайта
    в разделе LIMITED EDITION
    '''
    serializer_class = BannerSerializer

    def get_queryset(self):
        return Product.objects.filter(count__gt=0)[:4]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



class BannerView(ListAPIView):
    serializer_class = BannerSerializer
    def get_queryset(self):
        return Product.objects.filter(count__gt=0).order_by('-rating')[:4]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
