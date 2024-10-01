from django.urls import path
from .views import add_usuario, get_all_usuario, get_usuario, update_usuario, delete_usuario

urlpatterns = [
    path('usuario/add/', add_usuario, name='add_usuario'),
    path('usuario/all/', get_all_usuario, name='get_all_usuario'),
    path('usuario/<str:usuario_id>/', get_usuario, name='get_usuario'), 
    path('usuario/update/<str:usuario_id>/', update_usuario, name='update_usuario'),
    path('usuario/delete/<str:usuario_id>/', delete_usuario, name='delete_usuario'),
]
