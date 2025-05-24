from django.urls import path
from . import views

urlpatterns = [
    path('jezyki/', views.article_list, name='article_list'),
    path('jezyki/api/', views.get_articles)
]
