from django.db import models
from Profile.models import ShopUser

# Create your models here.
class Product(models.Model):
    PRODUCT_CATEGORIES = [
        ('L', 'Landschaft'),
        ('P', 'Portrait'),
        ('U', 'Urban'),
        ('S', 'Sport'),
        ('A', 'Artwork'),
        ('M', 'Makro'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    creator = models.ForeignKey(ShopUser,
                                on_delete=models.CASCADE,
                                related_name='user',
                                related_query_name='users')
    image = models.ImageField(null=True)
    category = models.CharField(max_length=1,
                                choices=PRODUCT_CATEGORIES,
                                )

    class Meta:
        ordering = ['creator', 'title']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class Vote(models.Model):
    VOTE_TYPES = [
        ('U', 'up'),
        ('D', 'down'),
    ]

    up_or_down = models.CharField(max_length=1,
                                  choices=VOTE_TYPES,
                                  )
    timestamp = models.DateTimeField(auto_now_add=True)
    shopUser = models.ForeignKey(ShopUser, on_delete=models.CASCADE)
    product =  models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.up_or_down + ' on ' + self.product.title + ' by ' + self.shopUser.username
