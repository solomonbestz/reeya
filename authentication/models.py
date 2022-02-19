from django.db import models
from datetime import datetime as d



date = d.now()



'''This is a class model representing my wholesellers db in postgres'''
class Wholseller(models.Model):
    wholeseller_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(default="email")
    password = models.CharField(max_length=20)
    date_of_joining = models.DateTimeField(default=date.strftime("%Y-%m-%d %H:%M:%S"))

'''This is a class model representing my resellers db in postgres'''
class Reseller(models.Model):
    reseller_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(default="email")
    password = models.CharField(max_length=20)
    date_of_joining = models.DateTimeField(default=date.strftime("%Y-%m-%d %H:%M:%S"))