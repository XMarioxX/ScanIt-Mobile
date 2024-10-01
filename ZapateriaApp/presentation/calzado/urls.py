from django.urls import path
from .views import add_calzado, get_all_calzado, get_calzado, update_calzado, delete_calzado

urlpatterns = [
    path('calzado/add/', add_calzado, name='add_calzado'),
    path('calzado/all/', get_all_calzado, name='get_all_calzado'),
    path('calzado/<str:calzado_id>/', get_calzado, name='get_calzado'), 
    path('calzado/update/<str:calzado_id>/', update_calzado, name='update_calzado'),
    path('calzado/delete/<str:calzado_id>/', delete_calzado, name='delete_calzado'),
]
