from djongo import models

# Create your models here.
class Author(models.Model):
    id =  models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    class Meta:
        db_table = "authors"

    def __str__(self):
        return self.name

class Publisher(models.Model):
    id =  models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    class Meta:
        db_table = "publishers"

    def __str__(self):
        return self.name

class Category(models.Model):
    id =  models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "categories"

    def __str__(self):
        return self.name
    
class Book(models.Model):
    id =  models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.IntegerField()
    sold = models.IntegerField(default=0)
    image = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = "books"
    
    def __str__(self):
        return self.title