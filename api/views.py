from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import HeroSerializer
from .models import Hero


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('my_data')
    serializer_class = HeroSerializer
    
    