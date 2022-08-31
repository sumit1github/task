from django.urls import path
from .views import AddProduct, UpdateProduct, Product_list
urlpatterns=[
    path('product',AddProduct.as_view(),name='product'),
    path('manage_product/<str:pid>',UpdateProduct.as_view(),name='manage_product'),
    path('product_list',Product_list.as_view()),
]