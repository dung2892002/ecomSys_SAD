from django.db import models

class CartItem(models.Model):
    user_id = models.CharField(max_length=20)
    product_type = models.CharField(max_length=50)
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "cart_items"