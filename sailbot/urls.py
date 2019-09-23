from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='sailbot-home'),
    path('about/', views.about, name='sailbot-about'),
    path('wind/', views.wind, name='sailbot-wind'),
    path('winchmotor/', views.winchmotor, name='sailbot-winchmotor'),
    path('ruddermotor/', views.winchmotor, name='sailbot-ruddermotor'),
    path('gps/', views.winchmotor, name='sailbot-gps'),
    path('boomangle/', views.winchmotor, name='sailbot-boomangle'),
    path('bms/', views.winchmotor, name='sailbot-bms'),
    path('accelerometer/', views.winchmotor, name='sailbot-accelerometer'),


]





