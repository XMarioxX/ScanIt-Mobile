from datetime import datetime
from pydantic import BaseModel, validator, constr
from typing import Optional

class ClienteApartadoValidator(BaseModel):
    nombre: constr(min_length=1, max_length=255)
    telefono: constr(min_length=10, max_length=15)  # Valida que el teléfono tenga entre 10 y 15 dígitos
    fechaCreate: Optional[str] = None
    fechaUpdate: Optional[str] = None

    @validator('telefono')
    def check_telefono(cls, v):
        if not v.isdigit():
            raise ValueError('El teléfono debe contener solo dígitos')
        return v
