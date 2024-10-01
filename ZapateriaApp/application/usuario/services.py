from ZapateriaApp.domain.usuario.models import Usuario
from ZapateriaApp.domain.usuario.repositories import UsuarioRepository
from ZapateriaApp.application.usuario.validators import UsuarioValidator
from datetime import datetime

class UsuarioService:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def add_usuario(self, data: dict) -> Usuario:
        validated_data = UsuarioValidator(**data)
        record = Usuario(
            **validated_data.dict(),
            fechaCreate=datetime.now().isoformat(),
            fechaUpdate=datetime.now().isoformat()
        )
        return self.repository.add(record)

    def update_usuario(self, usuario_id: str, data: dict) -> bool:
        validated_data = UsuarioValidator(**data)
        updated_data = Usuario(
            **validated_data.dict(),
            fechaUpdate=datetime.now().isoformat()
        )
        return self.repository.update(usuario_id, updated_data)
