from ZapateriaApp.domain.calzado.models import Calzado
from ZapateriaApp.domain.calzado.repositories import CalzadoRepository
from ZapateriaApp.application.calzado.validators import CalzadoValidator
from datetime import datetime

class CalzadoService:
    def __init__(self, repository: CalzadoRepository):
        self.repository = repository

    def add_calzado(self, data: dict) -> Calzado:
        validated_data = CalzadoValidator(**data)
        record = Calzado(
            **validated_data.dict(),
            fechaCreate=datetime.now().isoformat(),
            fechaUpdate=datetime.now().isoformat()
        )
        return self.repository.add(record)

    def update_calzado(self, calzado_id: str, data: dict) -> bool:
        validated_data = CalzadoValidator(**data)
        updated_data = Calzado(
            **validated_data.dict(),
            fechaUpdate=datetime.now().isoformat()
        )
        return self.repository.update(calzado_id, updated_data)
