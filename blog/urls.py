from django.urls import path,include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"Item", humanViewset)

urlpatterns = [
    path('items/', ItemsView.as_view(), name='items'),
    path('game/', Game.as_view(), name='game'),
    path('human',include(router.urls))
]