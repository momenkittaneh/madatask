from django.urls import path,include
from rest_framework import routers, urlpatterns
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()

router.register('customers',customerviewset,basename=customers)
router.register('services',serviceviewset,basename=service)


urlpatterns =[

    path('', include(router.urls)),

]