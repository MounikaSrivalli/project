# carreviews/urls.py

from django import views
from django.urls import path
from .views import CarReviewsList

urlpatterns = [
    path('reviews/', CarReviewsList.as_view(), name='car_reviews_list'),
]
