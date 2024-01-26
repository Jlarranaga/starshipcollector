from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('starships/', views.starships_index, name='index'),
    path('starships/<int:starship_id>', views.starships_detail, name='detail'),
    path('starships/create', views.StarshipCreate.as_view(), name='startships_create'),
    path('cats/<int:pk>/update', views.StarshipUpdate.as_view(), name='starships_update'),
    path('cats/<int:pk>/delete', views.StarshipDelete.as_view(), name='starships_delete'),
    path('cats/<int:starship_id>/add_maintenance', views.add_maintenance, name='add_maintenance'),
]