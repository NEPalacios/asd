from django.urls import path

from . import views

app_name ="stock"

urlpatterns = [
    
    path("stock/", views.home,name="index"),
]