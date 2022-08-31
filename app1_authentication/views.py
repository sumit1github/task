from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Product
from .serializer import ProductAddSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.generics import ListAPIView
class AddProduct(APIView):
    permission_classes = (IsAuthenticated,)
    pagination_class=LimitOffsetPagination
    model=Product
    serializer_class=ProductAddSerializer
    
    def post(self,request,*args,**kwargs):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            data=serializer.save()
            print(data.name)
            return Response({
                'status':status.HTTP_201_CREATED,
            })
        else:
            return Response({
                'status':status.HTTP_400_BAD_REQUEST,
                'errors':serializer.errors
            })
    

class Product_list(ListAPIView):
    queryset=Product.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class=LimitOffsetPagination
    model=Product
    serializer_class=ProductAddSerializer



class UpdateProduct(APIView):
    model=Product

    def post(self,request,*args,**kwargs):
        p_id=kwargs.get('pid')
        product=self.model.objects.get(id=p_id)
        name=request.data.get('name')

        product.name=name
        try:
            product.save()
            return Response({
                'status':status.HTTP_200_OK,
            })
        except Exception as e:
            return Response({
                'status':status.HTTP_400_BAD_REQUEST,
                'errors':str(e)
            })

    def delete(self,request,*args,**kwargs):
        p_id=kwargs.get('pid')
        product=self.model.objects.get(id=p_id)
        product.delete()

        return Response({
                'status':status.HTTP_200_OK,
                'message':'Product is deleted.'
            })
