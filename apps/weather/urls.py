from django.urls import path
from apps.weather import views
urlpatterns = [
    path('', views.home,name="home" ),
    
]
