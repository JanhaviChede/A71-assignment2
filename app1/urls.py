from django.urls import path
from .views import home, about,views

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
     path('debug-template/', views.debug_template, name='debug_template'),

]
