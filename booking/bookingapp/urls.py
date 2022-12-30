from django.contrib import admin
from django.urls import path
from .views import BookingappView
from .views import *

urlpatterns = [
    path('',BookingappView),
]