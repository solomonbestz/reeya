from django.db import models

# Create your models here.

class products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_des = models.CharField(max_length=200)
    product_price = models.IntegerField(max_length=20)
    
