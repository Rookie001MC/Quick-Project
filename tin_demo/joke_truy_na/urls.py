from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage_render, name="bulletin"),
    path("<int:pk>", views.prisoner_detail, name="prisoner_detail"),
    
]