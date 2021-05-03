from django.db import models

# Create your models here.
class Genres(models.Model):
    GenreId = models.AutoField(primary_key=True)
    GenreName = models.CharField(max_length=100)

class Books(models.Model):
    BookId = models.AutoField(primary_key=True)
    BookName = models.CharField(max_length=100)
    Availability = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    ReturnDate = models.DateField()
