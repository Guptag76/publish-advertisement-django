from django.db import models
import sys

# Create your models here.
class Hero(models.Model):
    my_data = models.CharField(max_length=sys.maxsize)
    
    def __str__(self):
        return self.my_data