from django.urls import path
from . import views


urlpatterns = [
    path('', views.exercise4, name='exercise4'),
    path('home', views.exercise4Home, name='exercise4Home'),
    path('productEntry', views.exercise4ProductEntry, name='exercise4ProductEntry'),
]
