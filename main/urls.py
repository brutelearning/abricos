from django.urls import path, include
from . import views

urlpatterns = [
    path('start/', views.start),
    path('schedule/', views.schedule)
]