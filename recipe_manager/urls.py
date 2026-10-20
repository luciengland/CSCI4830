from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_recipe, name='add_recipe'),
]