from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('starships/', views.starships_index, name='index'),
    path('starships/<int:starship_id>', views.starships_detail, name='detail')
]