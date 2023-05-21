from rest_framework import serializers
from .models import Product,Catagory,CustomerProfile,Orders,OrderItems,News,SubCatagory
from django.shortcuts import get_object_or_404

class CatagorySerilizer(serializers.ModelSerializer):
    class Meta:
        model=Catagory
        fields=['id','name','date','images']
class SubCatagorySerilizer(serializers.ModelSerializer):
    class Meta:
        model=SubCatagory
        fields=['id','name','date','images','catagory']
class ProductSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model=Product
        fields=['id','name','images','description','price','cattagory','date','discount','subcatagory']
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomerProfile
        fields=['id','Phone_no','user']
class OrderSerilizer(serializers.ModelSerializer):
    customer= serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=Orders
        fields=['orderuniqueId','customer','date_created','status','location',]
    def save(self, **kwargs):
        if self.context['userid']:
            (customer,created)=CustomerProfile.objects.get_or_create(user_id=self.context['userid'])
            if customer:
                self.validated_data['customer'] = customer
        return super().save(**kwargs)
class OrderItemSeializer(serializers.ModelSerializer):
    order=serializers.PrimaryKeyRelatedField(read_only=True)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
  
    class Meta:
        model=OrderItems
        fields=['id','order','product','quantity']
    def save(self, **kwargs):
       
       order=get_object_or_404(Orders, orderuniqueId=self.context['order_id'])
       if order:
            self.validated_data['order'] = order
       return super().save(**kwargs)
class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model=News
        fields=['id','Headline','description']

