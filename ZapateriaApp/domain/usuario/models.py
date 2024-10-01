from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class Usuario(BaseModel):
    id: Optional[str]
    nombre: str
    email: str
    password: str
    telefono: str
    fechaCreate: Optional[str] = None
    fechaUpdate: Optional[str] = None 

    def __init__(self, **data):
        super().__init__(**data)
        if not self.fechaCreate:
            self.fechaCreate = datetime.now().isoformat()
        if not self.fechaUpdate:
            self.fechaUpdate = datetime.now().isoformat()
