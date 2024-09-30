from django.urls import path
from .views import add_calzado, get_all_calzado, get_calzado, update_calzado, delete_calzado

urlpatterns = [
    path('', add_calzado, name='add_calzado'),
    path('all/', get_all_calzado, name='get_all_calzado'),
    path('<str:calzado_id>/', get_calzado, name='get_calzado'),
    path('update/<str:calzado_id>/', update_calzado, name='update_calzado'),
    path('delete/<str:calzado_id>/', delete_calzado, name='delete_calzado'),
]
