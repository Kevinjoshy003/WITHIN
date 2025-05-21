from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('log/', views.log_mood, name='log_mood'),
    path('history/', views.mood_history, name='mood_history'),
]
