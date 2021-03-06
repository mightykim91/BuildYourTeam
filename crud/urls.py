from django.urls import path
from . import views

app_name = 'crud'

urlpatterns = [
   path('', views.index, name='index'),
   path('detail/<int:player_pk>', views.detail, name='detail'),
   path('player_list/', views.player_list, name='player_list'),
]