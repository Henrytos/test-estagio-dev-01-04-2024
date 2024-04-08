from django.urls import path 
from .views import home , populate,list_consumers

urlpatterns  = [
    path("",home, name = "home"),
    path("populate/",populate, name = "populate"),
    path("consumers/",list_consumers, name = "consumers"),
    
]