from django.urls import path
from . import views


urlpatterns = [
    path('', views.exercise2, name='exercise2'),
    path('home', views.exercise2Home, name='exercise2Home'),
    path('livesEntry', views.exercise2LivesEntry, name='exercise2LivesEntry'),
    path('worksEntry', views.exercise2WorksEntry, name='exercise2WorksEntry'),
    path('companyEmployees', views.exercise2CompanyEmployees, name='exercise2CompanyEmployees')
]
