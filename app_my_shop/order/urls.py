from django.urls import path
from .views import OrderView, OrderDetailView


app_name = "order"

urlpatterns = [
    path('orders', OrderView.as_view(), name='orders'),
    path('order/<int:order_id>', OrderDetailView.as_view(), name='order-detail'),

]