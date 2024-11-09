from django.urls import path
from .views import traffic_data

urlpatterns = [
    path('traffic/', traffic_data),
]
