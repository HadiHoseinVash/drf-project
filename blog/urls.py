from django.urls import path
from .views import *


urlpatterns = [
    path('items/', ItemsView.as_view(), name='items'),
    path('game/', Game.as_view(), name='game'),
]