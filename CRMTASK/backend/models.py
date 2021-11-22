from os import name
from django.db import models




class employees(models.Model):
    email = models.EmailField(max_length=100)
    full_name=models.CharField(max_length=100)
    password= models.CharField(max_length=100)




class customers(models.Model):
    Male = 'Male'
    Female = 'Female'
    gender_choice=((Male,'Male'),(Female,'Female'))
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=25,choices=gender_choice,default=Male)
    age=models.IntegerField()
    company=models.CharField(max_length=100)
    service=models.ManyToManyField('service',related_name='service',blank=True)


class service(models.Model):
    name = models.CharField(max_length=100)
    customer=models.ManyToManyField(customers,related_name='customer',blank=True)


