from djongo import models


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    product_type = models.CharField(max_length=10)
    product_id = models.IntegerField()
    user_id = models.IntegerField()
    quantity = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)
    
    class Meta:
        db_table = "orders"
        
    def __str__(self) :
        return self.user_id