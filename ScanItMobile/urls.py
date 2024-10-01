from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('zapateria/', include('ZapateriaApp.presentation.calzado.urls')), 
    path('zapateria/', include('ZapateriaApp.presentation.proveedor.urls')), 
]
