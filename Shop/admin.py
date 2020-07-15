from django.contrib import admin
from Shop.models import Product, Vote, Vote_Comment, Order, OrderItem

# Register your models here.

admin.site.register(Product)
admin.site.register(Vote)
admin.site.register(Vote_Comment)
admin.site.register(Order)
admin.site.register(OrderItem)