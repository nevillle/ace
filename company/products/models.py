from django.db import models


# Create your models here.

class Product(models.Model):

    product_name = models.CharField(max_length=255,unique=True)
    comapny = models.ForeignKey('register.Company',on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product_name

