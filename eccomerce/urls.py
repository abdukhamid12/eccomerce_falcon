from django.urls import path
from eccomerce import views


app_name = 'store'
urlpatterns = [
    path('', views.store, name='store'),
    path('product_list/', views.product_list, name='product_list'),
    path('product_details/', views.product_details, name='product_details'),
]