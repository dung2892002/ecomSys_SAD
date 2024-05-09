from __future__ import unicode_literals
from django.db import models

class Fullname(models.Model):
    id= models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    class Meta:
        db_table = "fullname"
        
class Address(models.Model):
    id = models.AutoField(primary_key=True)
    no_house = models.CharField(max_length=10)
    street = models.CharField(max_length=50)
    ward = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    
    class Meta:
        db_table = "address"

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=255)
    
    class Meta:
        db_table = "accounts"

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=20)
    
    fullname = models.ForeignKey(Fullname, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "users"