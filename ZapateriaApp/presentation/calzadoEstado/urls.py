from django.urls import path
from .views import add_calzadoEstado, get_all_calzadoEstado, get_calzadoEstado, update_calzadoEstado, delete_calzadoEstado

urlpatterns = [
    path('calzadoEstado/add/', add_calzadoEstado, name='add_calzadoEstado'),
    path('calzadoEstado/all/', get_all_calzadoEstado, name='get_all_calzadoEstado'),
    path('calzadoEstado/<str:calzadoEstado_id>/', get_calzadoEstado, name='get_calzadoEstado'), 
    path('calzadoEstado/update/<str:calzadoEstado_id>/', update_calzadoEstado, name='update_calzadoEstado'),
    path('calzadoEstado/delete/<str:calzadoEstado_id>/', delete_calzadoEstado, name='delete_calzadoEstado'),
]
