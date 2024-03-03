from django.urls import path
from .views import *

urlpatterns = [
    path('ws/chat/<str:room_name>/',room)
]