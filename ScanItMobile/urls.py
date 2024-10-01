from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('zapateria/', include('ZapateriaApp.presentation.calzado.urls')), 
    path('zapateria/', include('ZapateriaApp.presentation.proveedor.urls')),
    path('zapateria/', include('ZapateriaApp.presentation.inversionista.urls')),
    path('zapateria/', include('ZapateriaApp.presentation.usuario.urls')),
    path('zapateria/', include('ZapateriaApp.presentation.clienteApartado.urls')),
    path('zapateria/', include('ZapateriaApp.presentation.calzadoTalla.urls')),
    path('zapateria/', include('ZapateriaApp.presentation.calzadoEstado.urls'))
]
