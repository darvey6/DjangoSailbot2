from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='sailbot-home'),
    path('about/', views.about, name='sailbot-about'),
    path('winchmotor/', views.winchmotor, name='sailbot-winchmotor')
]





