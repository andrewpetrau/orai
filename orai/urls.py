from django.urls import path
from . import views

urlpatterns = [
    path('', views.oru_prognose, name='oru_prognose'),
]
