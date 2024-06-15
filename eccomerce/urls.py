from django.urls import path
from eccomerce import views


app_name = 'store'
urlpatterns = [
    path('', views.store, name='store'),
    path('product_list/', views.product_list, name='product_list'),
    path('product_details/<int:pk>', views.product_details, name='product_details'),
    path('order_list/', views.order_list, name='order_list'),
    path('order_details/', views.order_details, name='order_details'),
    path('customers/', views.customers, name='customers'),
    path('customers_details/', views.customers_details, name='customers_details'),
    path('shopping_cart/', views.shopping_cart, name='shopping_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('billing/', views.billing, name='billing'),
    path('invoice/', views.invoice, name='invoice'),
]