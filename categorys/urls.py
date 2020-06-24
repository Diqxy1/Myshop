from django.urls import path, include
from . import views

urlpatterns = [
    path('list/', views.category_list, name='category_list'),
    path('create/', views.category_create, name='category_create'),
]
