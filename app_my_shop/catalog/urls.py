from django.urls import path
from .views import CategoriesView, CatalogView, BannerView, ProductsPopularView, ProductsLimitedView


app_name = "catalog"
urlpatterns = [
    # path('product/<int:product_id>/', ProductView.as_view(), name='product')
    path('categories', CategoriesView.as_view(), name='categories'),
    path('catalog', CatalogView.as_view(), name='catalog'),
    path('banners', BannerView.as_view(), name='banner'),
    path('products/popular', ProductsPopularView.as_view(), name='popular'),
    path('products/limited', ProductsLimitedView.as_view(), name='limited'),
]

