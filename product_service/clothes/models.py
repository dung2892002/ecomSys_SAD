from djongo import models

# Create your models here.
class Producer(models.Model):
    id =  models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    class Meta:
        db_table = "producers"

    def __str__(self):
        return self.name

class Style(models.Model):
    id =  models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "styles"

    def __str__(self):
        return self.name
    
class Clothes(models.Model):
    id =  models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    sold = models.IntegerField(default=0)
    quantity = models.IntegerField()
    image = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)

    class Meta:
        db_table = "clothes"
    
    def __str__(self):
        return self.title