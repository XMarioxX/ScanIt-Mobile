from datetime import datetime
from pydantic import BaseModel, validator, constr
from typing import Optional

class CalzadoTallaValidator(BaseModel):
    valueMX: constr(min_length=1, max_length=10)
    valueCN: constr(min_length=1, max_length=10)
    valueUS: constr(min_length=1, max_length=10)
    valueEU: constr(min_length=1, max_length=10)
    fechaCreate: Optional[str] = None
    fechaUpdate: Optional[str] = None

    @validator('valueMX', 'valueCN', 'valueUS', 'valueEU')
    def check_value(cls, v):
        if not v.replace('.', '', 1).isdigit(): 
            raise ValueError('El valor debe ser un número válido')
        return v