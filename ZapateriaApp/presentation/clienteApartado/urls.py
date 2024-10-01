from django.urls import path
from .views import add_clienteApartado, get_all_clienteApartado, get_clienteApartado, update_clienteApartado, delete_clienteApartado

urlpatterns = [
    path('clienteApartado/add/', add_clienteApartado, name='add_clienteApartado'),
    path('clienteApartado/all/', get_all_clienteApartado, name='get_all_clienteApartado'),
    path('clienteApartado/<str:clienteApartado_id>/', get_clienteApartado, name='get_clienteApartado'), 
    path('clienteApartado/update/<str:clienteApartado_id>/', update_clienteApartado, name='update_clienteApartado'),
    path('clienteApartado/delete/<str:clienteApartado_id>/', delete_clienteApartado, name='delete_clienteApartado'),
]
