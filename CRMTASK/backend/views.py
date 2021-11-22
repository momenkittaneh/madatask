from django.shortcuts import render

from .serializer import *
from rest_framework import viewsets
from .models import *



class customerviewset(viewsets.ModelViewSet):
    serializer_class = customersserializer
    queryset = customers.objects.all()

    