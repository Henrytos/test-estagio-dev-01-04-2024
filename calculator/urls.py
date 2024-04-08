from django.urls import path 
from .views import home , populate

urlpatterns  = [
    path("",home, name = "home"),
    path("populate/",populate, name = "populate"),
]