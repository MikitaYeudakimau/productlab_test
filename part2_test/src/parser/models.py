from django.db import models

class Product(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=100,blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10,blank=True,null=True)

    def __str__(self):
        return f"Product {self.name} with article {self.code}"

