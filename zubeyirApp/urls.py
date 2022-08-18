from django.contrib import admin
from django.urls import path, include
# from firstApp.views import home
# from secondApp.views import fshome
from .views import zubeyir_home

urlpatterns = [
    path("", zubeyir_home)
]