from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_request, name='create_request'),  # Create request
    path('track/', views.track_requests, name='track_requests'),  # Track requests
]
