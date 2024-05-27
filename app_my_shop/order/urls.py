from django.urls import path
from .views import OrderView


app_name = "order"

urlpatterns = [
    path('orders', OrderView.as_view(), name='orders'),

]