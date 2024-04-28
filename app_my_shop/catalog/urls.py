from django.urls import path
from .views import CategoriesView, CatalogView


app_name = "catalog"

urlpatterns = [
    # path('product/<int:product_id>/', ProductView.as_view(), name='product')
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('catalog/', CatalogView.as_view(), name='catalog')
]