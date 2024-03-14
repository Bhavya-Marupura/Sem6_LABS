from django.urls import path
from . import views


urlpatterns = [
    path('', views.exercise3, name='exercise3'),
    path('home', views.exercise3Home, name='exercise3Home'),
    path('authorEntry', views.exercise3AuthorEntry, name='exercise3AuthorEntry'),
    path('publisherEntry', views.exercise3PublisherEntry, name='exercise3PublisherEntry'),
    path('bookEntry', views.exercise3BookEntry, name='exercise3BookEntry'),
]
