from datetime import datetime
from pydantic import BaseModel, constr, validator
from typing import Optional
from enum import Enum

class TipoProveedor(str, Enum):
    MAYOREO = "mayoreo"
    MENUDEO = "menudeo"
    CONTADO = "contado"
    CREDITO = "credito"

class ProveedorValidator(BaseModel):
    id: Optional[str]
    nombre: constr(min_length=1, max_length=255)
    telefono: constr(min_length=10, max_length=15) 
    direccion: constr(min_length=1, max_length=255)
    tipo: TipoProveedor
    fechaCreate: Optional[str] = None
    fechaUpdate: Optional[str] = None

    @validator('telefono')
    def check_telefono(cls, v):
        if not v.isdigit():
            raise ValueError('El teléfono solo debe contener dígitos')
        return v

    def __init__(self, **data):
        super().__init__(**data)
        if not self.fechaCreate:
            self.fechaCreate = datetime.now().isoformat()
        if not self.fechaUpdate:
            self.fechaUpdate = datetime.now().isoformat()

