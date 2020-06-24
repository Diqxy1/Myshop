from django.urls import path, include
from . import views

urlpatterns = [
    path('categorys/', include('categorys.urls')),
    path('list', views.product_list, name='product_list'),
    path('create/', views.product_create, name='product_create'),
    path('update/', views.product_update, name='product_update'),
    path('delete/<int:id>', views.product_delete, name='product_delete'),
]
