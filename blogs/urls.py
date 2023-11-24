from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_articulos, name='articulos'),
]