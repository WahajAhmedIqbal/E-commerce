from django.db import models

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    pub_date = models.DateTimeField()
