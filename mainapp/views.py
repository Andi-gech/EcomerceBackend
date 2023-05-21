from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet,GenericViewSet
from rest_framework.mixins import RetrieveModelMixin,ListModelMixin,CreateModelMixin,UpdateModelMixin
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import CatagorySerilizer,ProductSerilizer,SubCatagorySerilizer,CustomerSerializer,OrderSerilizer,OrderItemSeializer,NewsSerializers
from .models import Product,Catagory,CustomerProfile,Orders,OrderItems,News,SubCatagory
from rest_framework.filters import SearchFilter,OrderingFilter
from django.db.models import Count
from mainapp.filters import ProductFilter 

from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class Catagoryviewset(ModelViewSet):
    queryset=Catagory.objects.all()
    serializer_class=CatagorySerilizer

class SubCatagoryviewset(ModelViewSet):
    def get_queryset(self):
        return SubCatagory.objects.filter(catagory=self.kwargs['catagory_pk'])
    serializer_class=SubCatagorySerilizer

class allproductViewset(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerilizer
    filter_backends=[DjangoFilterBackend,SearchFilter]
    filterset_class = ProductFilter
    search_fields=['name','description']
    
    
    
class Top_viewset(ReadOnlyModelViewSet):
    def get_queryset(self):
        top_products = OrderItems.objects \
            .values('product') \
            .annotate(total_orders=Count('product')) \
            .order_by('-total_orders')[:12]
        product_ids = [product['product'] for product in top_products]
        print( OrderItems.objects.all()) 
           
        return  Product.objects.filter(id__in=product_ids)
    
    serializer_class=ProductSerilizer
  
class NewProductViewset(ReadOnlyModelViewSet):
    def get_queryset(self):
        
        return Product.objects.all().order_by('-date')[:12]
    serializer_class=ProductSerilizer
    



class Productviewset(ModelViewSet):
    def get_queryset(self):
       
        return Product.objects.filter(cattagory=self.kwargs['catagory_pk'])
    serializer_class=ProductSerilizer
    filter_backends=[OrderingFilter]
   
    ordering_fields=['cattagory']
    def get_serializer_context(self):
        return {
            'catagory_id':self.kwargs['catagory_pk']
        }
    


class OrderViewsSet(ModelViewSet):
    def get_queryset(self):
        if(self.request.user.id):
            (customer,created)=CustomerProfile.objects.get_or_create(user_id=self.request.user.id)
            return Orders.objects.filter(customer=customer)
    permission_classes=[IsAuthenticated]
    queryset=Orders.objects.all()
    serializer_class=OrderSerilizer
   
    def get_serializer_context(self):
        return {
            'userid':self.request.user.id
        }
class OrderItemViewset(ModelViewSet):
    def get_queryset(self):
       
        return OrderItems.objects.filter(order=self.kwargs['order_pk'])
  
    serializer_class=OrderItemSeializer
    def get_serializer_context(self):
        return {
            'order_id':self.kwargs['order_pk']
        }

class Newsviewset(ModelViewSet):
    queryset=News.objects.all()
    serializer_class=NewsSerializers

class ProfileViewSet(CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,GenericViewSet):
    
   
    queryset=CustomerProfile.objects.all()
    serializer_class=CustomerSerializer
    @action(detail=False,methods=['GET','PUT'])
    def me(self ,request):
        (customerprofile,created)=CustomerProfile.objects.get_or_create(user_id=self.request.user.id)
        if request.method =='GET':
            serilizer=CustomerSerializer(customerprofile)
            return Response(serilizer.data)
        elif request.method=='PUT':
            serilizer=CustomerSerializer(customerprofile,data=request.data)
            serilizer.is_valid(raise_exception=True)
            serilizer.save()
            return Response(serilizer.data)