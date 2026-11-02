from django.urls import path
from MYApp import views


urlpatterns = [
     path("", views.home_view, name="homepage"),

    
]
