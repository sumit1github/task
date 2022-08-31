from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Product
from .serializer import ProductAddSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import pagination
from rest_framework.pagination import LimitOffsetPagination

class AddProduct(APIView, LimitOffsetPagination):
    permission_classes = (IsAuthenticated,)

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
    
    def get(self,request,*args,**kwargs):
        product=Product.objects.all()
        return Response({
            'status':status.HTTP_201_CREATED,
            'product_list':self.serializer_class(product,many=True).data
        })

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
