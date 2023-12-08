from django.urls import path

from . import views

app_name ="core"

urlpatterns = [
    
    path("", views.home_view, name="index"),
    path("stock/", views.stock_view, name="stock"),
    path("ver_stock/", views.stock_view, name="ver_stock"),
]