from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name="home"),
    path('create_poll/', create_view, name="create"),
    path('poll/<str:poll_id>', poll_view, name="poll"),
    path('results/<str:poll_id>', results_view, name="results"),
    path('stats/', stats_view, name="stats"),
]