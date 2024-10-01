from ZapateriaApp.domain.inversionista.models import Inversionista
from ZapateriaApp.domain.inversionista.repositories import InversionistaRepository
from ZapateriaApp.application.inversionista.validators import InversionistaValidator
from datetime import datetime

class InversionistaService:
    def __init__(self, repository: InversionistaRepository):
        self.repository = repository

    def add_inversionista(self, data: dict) -> Inversionista:
        validated_data = InversionistaValidator(**data)
        record = Inversionista(
            **validated_data.dict(),
            fechaCreate=datetime.now().isoformat(),
            fechaUpdate=datetime.now().isoformat()
        )
        return self.repository.add(record)

    def update_inversionista(self, inversionista_id: str, data: dict) -> bool:
        validated_data = InversionistaValidator(**data)
        updated_data = Inversionista(
            **validated_data.dict(),
            fechaUpdate=datetime.now().isoformat()
        )
        return self.repository.update(inversionista_id, updated_data)
