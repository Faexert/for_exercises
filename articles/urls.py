from django.urls import path # to upload data from the database to the page

from .views import *

urlpatterns = [
    path('cars/', CarView.as_view(), name='list_cars'),
]