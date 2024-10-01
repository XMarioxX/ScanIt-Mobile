from datetime import datetime
from pydantic import BaseModel, constr, EmailStr, validator
import bcrypt
from typing import Optional

class UsuarioValidator(BaseModel):
    id: Optional[str]
    nombre: constr(min_length=1, max_length=255) 
    email: EmailStr 
    password: str 
    telefono: constr(min_length=10, max_length=15) 
    fechaCreate: Optional[str] = None
    fechaUpdate: Optional[str] = None

    @validator('password', pre=True)
    def hash_password(cls, v):
        if not v.startswith('$2b$'):
            hashed = bcrypt.hashpw(v.encode('utf-8'), bcrypt.gensalt())
            return hashed.decode('utf-8')
        return v
    
    @validator('telefono')
    def check_telefono(cls, v):
        if not v.isdigit():
            raise ValueError('El teléfono debe contener solo números')
        return v
