from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class CustomerProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    
    Phone_no= models.CharField(max_length=20)
    def __str__(self) :
        return self.user.username
class Catagory(models.Model):
    name=models.CharField(max_length=255)
    images=models.ImageField(upload_to='user/profile_pic',null=True)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class SubCatagory(models.Model):
    name=models.CharField(max_length=255)
    catagory=models.ForeignKey(Catagory,on_delete=models.CASCADE)
    images=models.ImageField(upload_to='user/profile_pic',null=True)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class Product(models.Model):
    name=models.CharField(max_length=255)
    images=models.ImageField(upload_to='user/profile_pic',null=True)
    date=models.DateTimeField(auto_now_add=True)
    description=models.TextField()
    price= models.DecimalField(max_digits=8, decimal_places=2)
    discount=models.IntegerField()
    subcatagory=models.ForeignKey(SubCatagory,on_delete=models.CASCADE,default=1)
    cattagory=models.ForeignKey(Catagory,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class Orders(models.Model):
    status_CHOICES = (
        ('aproved', 'aproved'),
        ('pending', 'pending'),
        ('declined', 'declined'),
    )
    
    orderuniqueId=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  
    location=models.CharField(max_length=255)
    customer=models.ForeignKey(CustomerProfile,on_delete=models.CASCADE,null=True,blank=True)
    date_created=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=10, choices=status_CHOICES,default="pending")
    def __str__(self):
        return str(self.orderuniqueId)
class OrderItems(models.Model):
    order=models.ForeignKey(Orders,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    def __str__(self) :
        return str(self.order.orderuniqueId)
class News(models.Model):
    Headline=models.CharField(max_length=1000)
    description=models.TextField()
    def __str__(self) :
        return self.Headline



  