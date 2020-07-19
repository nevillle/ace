from django.db import models

# Create your models here.


class PurchaseOrder(models.Model):

    product = models.ForeignKey('products.Product',on_delete=models.CASCADE)
    comapny = models.ForeignKey('register.Company',on_delete=models.CASCADE)
    qty = models.IntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    po_no = models.CharField(max_length=255,default="missing")

    def __str__(self):
        return str(self.product)