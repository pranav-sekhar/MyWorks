from django.db import models
from django.contrib.auth.models import User #import user model

class Category(models.Model):
    genre = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.genre

class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='posters/',blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    release_date = models.DateField()
    actors = models.CharField(max_length=100)
    rating = models.FloatField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE) #connects catgeory to genre in Category
    trailer = models.URLField() 
    added_by = models.ForeignKey(User,on_delete=models.CASCADE) #connects to user who added it

    def __str__(self):
        return self.title
    