from ZapateriaApp.domain.clienteApartado.models import ClienteApartado
from ZapateriaApp.domain.clienteApartado.repositories import ClienteApartadoRepository
from ZapateriaApp.application.clienteApartado.validators import ClienteApartadoValidator
from datetime import datetime

class ClienteApartadoService:
    def __init__(self, repository: ClienteApartadoRepository):
        self.repository = repository

    def add_clienteApartado(self, data: dict) -> ClienteApartado:
        validated_data = ClienteApartadoValidator(**data)
        record = ClienteApartado(
            **validated_data.dict(),
            fechaCreate=datetime.now().isoformat(),
            fechaUpdate=datetime.now().isoformat()
        )
        return self.repository.add(record)

    def update_clienteApartado(self, clienteApartado_id: str, data: dict) -> bool:
        validated_data = ClienteApartadoValidator(**data)
        updated_data = ClienteApartado(
            **validated_data.dict(),
            fechaUpdate=datetime.now().isoformat()
        )
        return self.repository.update(clienteApartado_id, updated_data)
