from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TaskList(models.Model):
    owner = models.ForeignKey(User, on_delete= models.CASCADE, default= None)
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.task

class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length = 254)
    sub = models.TextField()
    query = models.TextField()
    
    def __str__(self):
        return self.name
