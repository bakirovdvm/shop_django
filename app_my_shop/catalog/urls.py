from django.urls import path
from .views import CategoriesView


app_name = "catalog"

urlpatterns = [
    # path('product/<int:product_id>/', ProductView.as_view(), name='product')
    path('categories/', CategoriesView.as_view(), name='categories')
]