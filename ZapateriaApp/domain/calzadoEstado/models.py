from datetime import datetime
from pydantic import BaseModel, validator
from typing import Optional

class CalzadoValidator(BaseModel):
    id: Optional[str]
    active: bool
    inactive: bool
    deleted: bool
    fechaCreate: Optional[str] = None
    fechaUpdate: Optional[str] = None

    @validator('active', 'inactive', 'deleted')
    def check_boolean(cls, v):
        if not isinstance(v, bool):
            raise ValueError('El valor debe ser booleano')
        return v

    @validator('active')
    def check_active_inactive_status(cls, v, values):
        if v and ('inactive' in values and values['inactive']):
            raise ValueError('No puede estar activo e inactivo al mismo tiempo')
        return v

    @validator('inactive')
    def check_inactive_active_status(cls, v, values):
        if v and ('active' in values and values['active']):
            raise ValueError('No puede estar inactivo y activo al mismo tiempo')
        return v

    @validator('deleted')
    def check_deleted_status(cls, v, values):
        if v and ('active' in values and values['active']):
            raise ValueError('No puede estar eliminado y activo al mismo tiempo')
        return v
