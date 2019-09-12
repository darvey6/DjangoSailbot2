from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('sensors/', views.sensors, name='blog-sensors'),
    path('winchmotor/', views.winchmotor, name='blog-winchmotor')
]





