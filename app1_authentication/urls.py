from django.urls import path
from .views import AddProduct, UpdateProduct
urlpatterns=[
    path('product',AddProduct.as_view(),name='product'),
    path('manage_product/<str:pid>',UpdateProduct.as_view(),name='manage_product'),
]