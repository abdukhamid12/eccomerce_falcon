from django.urls import path
from eccomerce import views


app_name = 'store'
urlpatterns = [
    path('', views.store, name='store'),
]