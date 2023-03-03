from django.db import models

class Product(models.Model):
    article = models.IntegerField()
    brand = models.CharField(max_length=100,blank=True)
    title = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return f"Product {self.brand} with article {self.article}"

