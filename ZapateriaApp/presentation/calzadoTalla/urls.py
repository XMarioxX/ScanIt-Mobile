from django.urls import path
from .views import add_calzadoTalla, get_all_calzadoTalla, get_calzadoTalla, update_calzadoTalla, delete_calzadoTalla

urlpatterns = [
    path('calzadoTalla/add/', add_calzadoTalla, name='add_calzadoTalla'),
    path('calzadoTalla/all/', get_all_calzadoTalla, name='get_all_calzadoTalla'),
    path('calzadoTalla/<str:calzadoTalla_id>/', get_calzadoTalla, name='get_calzadoTalla'), 
    path('calzadoTalla/update/<str:calzadoTalla_id>/', update_calzadoTalla, name='update_calzadoTalla'),
    path('calzadoTalla/delete/<str:calzadoTalla_id>/', delete_calzadoTalla, name='delete_calzadoTalla'),
]
