from django.contrib import admin
from .models import Catagory,Product,Orders,OrderItems,News,CustomerProfile,SubCatagory
admin.site.register(CustomerProfile)
admin.site.register(Catagory)
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(OrderItems)
admin.site.register(News)
admin.site.register(SubCatagory)
# Register your models here.
