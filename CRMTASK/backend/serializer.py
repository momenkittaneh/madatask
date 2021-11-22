from django.db.models import fields
from .models import *
from rest_framework import serializers

class customersserializer (serializers.ModelSerializer):
    class Meta:
        model = customers
        fields=('id','name','gender','age','company','service')
        