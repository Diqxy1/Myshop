from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('category/', views.category_create, name='category_create'),
    path('create/', views.product_create, name='product_create'),
    path('update/', views.product_update, name='product_update'),
    path('delete/<int:id>', views.product_delete, name='product_delete'),
]
