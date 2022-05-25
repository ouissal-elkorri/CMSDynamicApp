from . import views
from django.urls import path

urlpatterns = [
    path('', views.list_menu),
    path('menu/<str:pk>/', views.list_sous_menu, name='menu'),
    path('sous_menu/<str:pk>/', views.list_articles, name='sous_menu')
]
