from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),       # sends the url to the views.homepage function
    path('foo/', views.foo),
    path('countz/', views.count, name='count'),
    path('about/', views.about, name='about')
]
