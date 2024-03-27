from django.urls import path
from chatapp.views import home

urlpatterns = [
    path('',home,name="home"),
]