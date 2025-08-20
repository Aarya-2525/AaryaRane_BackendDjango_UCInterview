from django.urls import path
from . import views

urlpatterns = [
    path("search/", views.cocktails_search, name="cocktails_search"),
    path("detail/<int:cocktail_id>/", views.cocktail_detail, name="cocktail_detail"),
    path("popular/", views.popular_cocktails, name="popular_cocktails"),
]