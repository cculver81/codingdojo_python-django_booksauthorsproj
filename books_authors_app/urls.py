from django.urls import path
from books_authors_app import views

urlpatterns = [
    path('', views.index)
]