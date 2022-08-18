from django.urls import path
# from firstApp.views import home
# from secondApp.views import fshome
from .views import home

urlpatterns = [
    path('', home),
    ]
