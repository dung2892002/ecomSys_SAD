from django.db import models

# Create your models here.
class Shipment(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=10)
    order_id = models.CharField(max_length=10)
    payment_id = models.CharField(max_length=10)
    status = models.CharField(default="Ready to dispatch", max_length=50)
    
    class Meta:
        db_table = "shipments"