from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add_calzado),
    path('showAll', views.get_all_calzado),
]
