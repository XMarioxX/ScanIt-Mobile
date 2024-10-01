from pydantic import BaseModel, validator, constr
from typing import Optional

class InversionistaValidator(BaseModel):
    id: Optional[str]
    nombre: constr(min_length=1, max_length=255)  
    presupuesto: float 
    fechaCreate: Optional[str] = None
    fechaUpdate: Optional[str] = None

    @validator('presupuesto')
    def check_presupuesto(cls, v):
        if v < 0:
            raise ValueError('El presupuesto debe ser mayor o igual a 0')
        return v
