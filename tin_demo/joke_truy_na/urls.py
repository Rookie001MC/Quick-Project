from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage_render.as_view(), name="bulletin"),
    path("<int:pk>", views.prisoner_detail.as_view(), name="prisoner_detail"),
    
    
]