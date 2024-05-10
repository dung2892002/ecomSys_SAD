from django.db import models

class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=10)
    order_id = models.CharField(max_length=10)
    mode_of_payment = models.CharField(max_length=20)
    status = models.CharField(max_length=15)
    
    class Meta:
        db_table = "payments"
