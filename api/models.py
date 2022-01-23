from django.db import models
import sys

# Create your models here.
class Hero(models.Model):
    my_data = models.TextField(max_length=100000)
    
    def __str__(self):
        return self.my_data