from django.urls import path
from chatapp.views import home,checkview

urlpatterns = [
    path('',home,name="home"),
    path("<str:room>/",home,name="home"),
    path("checkview",checkview,name="checkview")
]