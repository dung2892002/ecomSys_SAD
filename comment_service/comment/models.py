from django.db import models

class Comment(models.Model):
    user_id = models.CharField(max_length=20)
    product_type = models.CharField(max_length=50)
    product_id = models.IntegerField()
    content = models.CharField(max_length=8200)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "comments"