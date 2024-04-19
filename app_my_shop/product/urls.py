from django.urls import path
from .views import ProductView

app_name = "product"

urlpatterns = [
    path('product/<int:product_id>/', ProductView.as_view(), name='product')
]