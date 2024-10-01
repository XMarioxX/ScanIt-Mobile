from django.urls import path
from .views import add_inversionista, get_all_inversionista, get_inversionista, update_inversionista, delete_inversionista

urlpatterns = [
    path('inversionista/add/', add_inversionista, name='add_inversionista'),
    path('inversionista/all/', get_all_inversionista, name='get_all_inversionista'),
    path('inversionista/<str:inversionista_id>/', get_inversionista, name='get_inversionista'), 
    path('inversionista/update/<str:inversionista_id>/', update_inversionista, name='update_inversionista'),
    path('inversionista/delete/<str:inversionista_id>/', delete_inversionista, name='delete_inversionista'),
]
