from pydantic import BaseModel, validator, constr
from typing import Optional

class CalzadoValidator(BaseModel):
    nombre: constr(min_length=1, max_length=255)  
    codigoBarras: constr(min_length=1, max_length=255)  
    proveedores: constr(min_length=1, max_length=255)  
    inversionistas: float  
    cantidad: int  
    precioCompra: float  
    precioVenta: float  
    estado: constr(min_length=1, max_length=50)  
    fechaCreate: Optional[str] = None 
    fechaUpdate: Optional[str] = None 

    @validator('precioVenta')
    def check_precio_venta(cls, v, values):
        if v < 0:
            raise ValueError('El precio de venta debe ser mayor o igual a 0')
        if 'precioCompra' in values and v < values['precioCompra']:
            raise ValueError('El precio de venta debe ser mayor o igual al precio de compra')
        return v

    @validator('cantidad')
    def check_cantidad(cls, v):
        if v < 0:
            raise ValueError('La cantidad debe ser mayor o igual a 0')
        return v
