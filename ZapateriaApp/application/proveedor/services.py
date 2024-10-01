from ZapateriaApp.domain.proveedor.models import Proveedor
from ZapateriaApp.domain.proveedor.repositories import ProveedorRepository
from ZapateriaApp.application.proveedor.validators import ProveedorValidator
from datetime import datetime

class ProveedorService:
    def __init__(self, repository: ProveedorRepository):
        self.repository = repository

    def add_proveedor(self, data: dict) -> Proveedor:
        validated_data = ProveedorValidator(**data)
        record = Proveedor(
            **validated_data.dict(),
            fechaCreate=datetime.now().isoformat(),
            fechaUpdate=datetime.now().isoformat()
        )
        return self.repository.add(record)

    def update_proveedor(self, proveedor_id: str, data: dict) -> bool:
        validated_data = ProveedorValidator(**data)
        updated_data = Proveedor(
            **validated_data.dict(),
            fechaUpdate=datetime.now().isoformat()
        )
        return self.repository.update(proveedor_id, updated_data)
