from django.urls import path
from .views import add_proveedor,get_all_proveedor,get_provedor,update_proveedor,delete_proveedor

urlpatterns = [
    path('proveedor/add/', add_proveedor, name='add_proveedor'),
    path('proveedor/all/', get_all_proveedor, name='get_all_proveedor'),
    path('proveedor/<str:proveedor_id>/', get_provedor, name='get_proveedor'), 
    path('proveedor/update/<str:proveedor_id>/', update_proveedor, name='update_proveedor'),
    path('proveedor/delete/<str:proveedor_id>/', delete_proveedor, name='delete_proveedor'),
]
