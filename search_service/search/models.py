from django.db import models

class Search(models.Model):
    key = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    user_id = models.CharField(max_length=7)

    def __str__(self):
        return self.key
