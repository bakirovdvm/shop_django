from django.urls import path
from .views import ProductView, ProductReview

app_name = "product"

urlpatterns = [
    path('product/<int:product_id>/', ProductView.as_view(), name='product'),
    path('product/<int:id>/reviews', ProductReview.as_view(), name='product_review'),
]