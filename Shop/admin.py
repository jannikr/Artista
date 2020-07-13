from django.contrib import admin
from Shop.models import Product, Vote, Vote_Comment

# Register your models here.

admin.site.register(Product)
admin.site.register(Vote)
admin.site.register(Vote_Comment)