from __future__ import unicode_literals
from django.db import models

class payment_status(models.Model):
    username = models.CharField(max_length=255)
    product_type = models.CharField(max_length=60)
    product_id = models.CharField(max_length=10)
    price = models.CharField(max_length=10)
    quantity = models.CharField(max_length=5)
    mode_of_payment = models.CharField(max_length=20)
    mobile = models.CharField(max_length=12)
    status = models.CharField(max_length=15)
    
    class Meta:
        db_table = "payments"
        
    def __str__(self):
        return '%s %s %s %s %s %s %s ' % (self.username, self.product_type, self.product_id, self.price, 
                                          self.quantity, self.mode_of_payment, self.mobile, self.status)