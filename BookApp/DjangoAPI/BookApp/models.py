from django.db import models

# Create your models here.

class Books(models.Model):
    BookId = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=500)
    Author = models.CharField(max_length=500)
    Genre = models.CharField(max_length=500)
    Favorite=models.BooleanField(default=True)