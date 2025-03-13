from django.urls import path
from .views import *

urlpatterns = [
    path('brands/', brands, name='brands'),
    path('car_profile/<pk>/', car_profile, name='car-profile'),
    path('', main_page, name='main'),
]