from django.urls import path
from .views import cocktails_search

urlpatterns = [
    path('search/', cocktails_search, name='cocktails_search'),
]