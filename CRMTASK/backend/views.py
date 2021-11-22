from django.shortcuts import render

from .serializer import *
from rest_framework import viewsets,filters
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination

class customerpagin(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10

class customerviewset(viewsets.ModelViewSet):
    serializer_class = customersserializer
    queryset = customers.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name')
    pagination_class = customerpagin

class serviceviewset(viewsets.ModelViewSet):
    serializer_class = serviceserializer
    queryset = service.objects.all()
