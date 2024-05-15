

from django.http import JsonResponse, HttpResponse

from rest_framework import permissions, generics
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from product.models import Product, ProductReview, ProductSale
from product.serializers import ProductSerializer, ProductSaleSerializer
from .serializers import ProductsPopularSerializer, BannerSerializer, CatalogSerizlizer

from .models import Category, Subcategory, CategoryImage, SubCategoryImage


class CategoriesView(APIView):
    '''
    Описывается отображение категорий в выпадающем меню сайта, где орображаются
    категории и под-категории товаров, а также картинки-превьюшкни к ним
    '''
    def get(self, request):
        categories = Category.objects.all()
        # print('\ncategories'.upper(), categories)
        categories_data = []

        for category in categories:
            subcategories = category.subcategory.all()
            # print('\nsubcategories'.upper(), subcategories)
            subcategories_data = []

            for subcategory in subcategories:
                data_subcat = {
                    "id": subcategory.pk,
                    "title": subcategory.title,
                    "image": subcategory.get_image(),
                }
                subcategories_data.append(data_subcat)
                # print('\nsubcategories_data'.upper(), subcategories_data)

            data_category = {
                "id": category.pk,
                "title": category.title,
                "image": category.get_image(),
                "subcategories": subcategories_data,
            }
            categories_data.append(data_category)

        return JsonResponse(categories_data, safe=False)


class CatalogView(APIView):
    '''
    Описывается работа фильтров по имени, минимальной и максимальной цене, способе доставки и
    популярным тегам товаров
    '''
    def get(self, request):

        filter_name = request.query_params.get("filter[name]", "")
        min_price = request.query_params.get("filter[minPrice]", 0)
        max_price = request.query_params.get("filter[maxPrice]", 50000)
        free_delivery = request.query_params.get("filter[freeDelivery]", False)
        available = request.query_params.get("filter[available]", True)
        tags = request.query_params.getlist("tags[]")
        # tags = request.query_params.get('filter[tags]', True)
        print("tags", tags)
        queryset = Product.objects

        if tags:
            queryset = queryset.filter(tags__id__in=tags)

        if free_delivery == "false":
            queryset = queryset.filter(freeDelivery=False)
        else:
            queryset = queryset.filter(freeDelivery=True)

        if filter_name:
            queryset = queryset.filter(title__icontains=filter_name)

        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        print("queryset", queryset.distinct())
        serializer = ProductSerializer(queryset.distinct(), many=True)

        request_data = {
            "items": serializer.data,
            "currentPage": request.query_params.get("currentPage"),
            "lastPage": request.query_params.get("lastPage"),
        }
        return Response(request_data)


class BannerView(ListAPIView):
    '''
    Описывается отображение товаров/продуктов в верхней части главной страницы, где по клику
    можно попасть на страницу с фильтрами, чтобо найти нужный продукт по цене, имени и тэгам
    '''
    serializer_class = BannerSerializer

    def get_queryset(self):
        return Product.objects.filter(count__gt=0).order_by("-rating")[:4]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ProductsPopularView(ListAPIView):
    '''
    Описывается отображение популярных товаров/продуктов на главной странице сайта
    в разделе POPULAR PRODUCTS
    '''
    serializer_class = BannerSerializer

    def get_queryset(self):
        return Product.objects.filter(count__gt=0)[:1]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        # print('serializer.data'.upper(), serializer.data)
        return Response(serializer.data)


class LimitedView(ListAPIView):
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


class ProductPagination(PageNumberPagination):
    '''
    Описывается работа пагинации для страницы Распродажи .../sale/

    '''
    page_size_query_param = "limit"
    page_size = 2
    page_query_param = "currentPage"
    max_page_size = 100

    def get_paginated_response(self, data) -> Response:
        modified_data = []
        # Изменение данных в каждом элементе
        for item in data:
            item["images"] = item["product"]["images"]
            item["title"] = item["product"]["title"]
            item.pop("product", None)
            modified_data.append(item)

        return Response(
            {
                "items": data,
                "currentPage": self.page.number,
                "lastPage": self.page.paginator.num_pages,
            }
        )


class SaleView(generics.ListCreateAPIView):
    '''
    Описывается отображение страницы .../sale/, где находятся продукты/товары,
    которые находятся на распродаже.

    Распродажа настраивается в соответствующем поле в админке, то есть добавить
    товар/продукт на распродажу, можно зайти в админку, затем находим раздел PRODUCT, далее Product sales
    и после уже добавляете товар из выпадающего меню всех доступных товаров, устанаваливаете
    свою цену, даты распродажы и сохраняете.
    '''
    queryset = ProductSale.objects.filter(is_on_sale=True)
    serializer_class = ProductSaleSerializer
    pagination_class = ProductPagination

