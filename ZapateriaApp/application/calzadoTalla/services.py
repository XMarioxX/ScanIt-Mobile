from ZapateriaApp.domain.calzadoTalla.models import CalzadoTalla
from ZapateriaApp.domain.calzadoTalla.repositories import CalzadoTallaRepository
from ZapateriaApp.application.calzadoTalla.validators import CalzadoTallaValidator
from datetime import datetime

class CalzadoTallaService:
    def __init__(self, repository: CalzadoTallaRepository):
        self.repository = repository

    def add_calzadoTalla(self, data: dict) -> CalzadoTalla:
        validated_data = CalzadoTallaValidator(**data)
        record = CalzadoTalla(
            **validated_data.dict(),
            fechaCreate=datetime.now().isoformat(),
            fechaUpdate=datetime.now().isoformat()
        )
        return self.repository.add(record)

    def update_calzadoTalla(self, calzadoTalla_id: str, data: dict) -> bool:
        validated_data = CalzadoTallaValidator(**data)
        updated_data = CalzadoTalla(
            **validated_data.dict(),
            fechaUpdate=datetime.now().isoformat()
        )
        return self.repository.update(calzadoTalla_id, updated_data)
