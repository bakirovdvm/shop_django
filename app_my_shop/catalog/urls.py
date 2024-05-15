
from django.urls import path
from .views import (
    CategoriesView,
    CatalogView,
    ProductsPopularView,
    BannerView,
    # ProductsLimitedView
    LimitedView,
    SaleView,
)

app_name = "catalog"

urlpatterns = [
    path("categories/", CategoriesView.as_view(), name="categories"),
    path("catalog/", CatalogView.as_view(), name="catalog"),
    path("products/popular/", ProductsPopularView.as_view(), name="productsPopular"),
    path("products/limited/", LimitedView.as_view(), name="limited"),
    path("banners/", BannerView.as_view(), name="banners"),
    path("sales/", SaleView.as_view(), name="sales"),
]
