from django.urls import path
from . import views


urlpatterns = [
    path('', views.exercise1, name='exercise1'),
    path('/home', views.exercise1Home, name='exercise1Home'),
    path('/categoryEntry', views.exercise1CategoryEntry, name='exercise1CategoryEntry'),
    path('/pageEntry', views.exercise1PageEntry, name='exercise1PageEntry')
]
