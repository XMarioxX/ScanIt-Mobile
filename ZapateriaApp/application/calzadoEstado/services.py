from ZapateriaApp.domain.calzadoEstado.models import CalzadoEstado
from ZapateriaApp.domain.calzadoEstado.repositories import CalzadoEstadoRepository
from ZapateriaApp.application.calzadoEstado.validators import CalzadoEstadoValidator
from datetime import datetime

class CalzadoEstadoService:
    def __init__(self, repository: CalzadoEstadoRepository):
        self.repository = repository

    def add_calzadoEstado(self, data: dict) -> CalzadoEstado:
        validated_data = CalzadoEstadoValidator(**data)
        record = CalzadoEstado(
            **validated_data.dict(),
            fechaCreate=datetime.now().isoformat(),
            fechaUpdate=datetime.now().isoformat()
        )
        return self.repository.add(record)

    def update_calzadoEstado(self, calzadoEstado_id: str, data: dict) -> bool:
        validated_data = CalzadoEstadoValidator(**data)
        updated_data = CalzadoEstado(
            **validated_data.dict(),
            fechaUpdate=datetime.now().isoformat()
        )
        return self.repository.update(calzadoEstado_id, updated_data)
