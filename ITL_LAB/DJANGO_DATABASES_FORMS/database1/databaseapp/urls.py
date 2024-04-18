
from django.urls import path
from . import views
urlpatterns = [
    path('home',views.home,name='home'),
    path('display',views.display,name="display"),
    path('worksentry',views.worksentry,name='worksentry'),
    path('livesentry',views.livesentry,name="livesentry"),
    path('companydisplay',views.companyemployees,name="companydisplay"),
    path('deleterow/<int:pk>',views.deleterow,name='deleterow'),
    path('updaterow/<int:pk>',views.updaterow,name='updaterow'),
]
