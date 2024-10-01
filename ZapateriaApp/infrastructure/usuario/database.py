from bson import ObjectId
from pymongo import MongoClient
from typing import List, Optional
from ZapateriaApp.domain.usuario.models import Usuario
from ZapateriaApp.domain.usuario.repositories import UsuarioRepository

class MongoUsuarioRepository(UsuarioRepository):
    def __init__(self, db: MongoClient):
        self.collection = db.usuario_collection

    def add(self, usuario: Usuario) -> Usuario:
        record = usuario.dict(exclude_unset=True)
        result = self.collection.insert_one(record)
        record["id"] = str(result.inserted_id)
        return Usuario(**record)

    def get_all(self) -> List[Usuario]:
        return [
            Usuario(**{**usuario, "id": str(usuario["_id"])}) 
            for usuario in self.collection.find()
        ]

    def get(self, usuario_id: str) -> Optional[Usuario]:
        usuario = self.collection.find_one({"_id": ObjectId(usuario_id)})
        if usuario:
            return Usuario(**{**usuario, "id": str(usuario["_id"])})
        return None

    def update(self, usuario_id: str, usuario: Usuario) -> bool:
        result = self.collection.update_one(
            {"_id": ObjectId(usuario_id)}, 
            {"$set": usuario.dict(exclude_unset=True)}
        )
        return result.matched_count > 0

    def delete(self, usuario_id: str) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(usuario_id)})
        return result.deleted_count > 0
