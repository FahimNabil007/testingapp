from django.db import models

# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=300, unique=True)
    content= models.TextField()
    Bug_status= models.CharField(max_length=50, default='enter your progress')