from rest_framework import serializers

from .models import Product

class ProductAddSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
        extra_kwargs={'name':{'required':True}}
        
    
    def validate_name(self,name):
        if name:
            if (Product.objects.filter(name=name).exists())==True:
                serializers.ValidationError({'message':'Projrct name should be Unique'})
        else:
            serializers.ValidationError({'message':'Name is needed'})
        
        return name
