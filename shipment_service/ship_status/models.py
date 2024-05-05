from __future__ import unicode_literals
from django.db import models

class shipment(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=12)
    address = models.CharField(max_length=200)
    product_id = models.CharField(max_length=10)
    product_type = models.CharField(max_length=100)
    quantity = models.CharField(max_length=5) 
    payment_status = models.CharField(max_length=15)
    transaction_id = models.CharField(max_length=5)
    shipment_status = models.CharField(max_length=20)
    
    class Meta:
        db_table = "shipment"
    
    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s %s %s' % (self.fname, self.lname, self.email, self.mobile, self.product_type, self.product_id, self.address, self.quantity , self.payment_status, self.transaction_id, self.shipment_status)