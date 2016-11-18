from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=128, unique=True)
    authorname = models.CharField(max_length=128)
    Publisher = models.CharField(max_length=128)
    Date = models.DateField()
    version = models.CharField(max_length=128)
    price = models.IntegerField()
    
    def __str__(self):
        return self.title
    