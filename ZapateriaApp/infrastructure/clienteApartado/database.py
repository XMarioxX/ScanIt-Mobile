from bson import ObjectId
from pymongo import MongoClient
from typing import List, Optional
from ZapateriaApp.domain.clienteApartado.models import ClienteApartado
from ZapateriaApp.domain.clienteApartado.repositories import ClienteApartadoRepository

class MongoClienteApartadoRepository(ClienteApartadoRepository):
    def __init__(self, db: MongoClient):
        self.collection = db.clienteApartado_collection

    def add(self, clienteApartado: ClienteApartado) -> ClienteApartado:
        record = clienteApartado.dict(exclude_unset=True)
        result = self.collection.insert_one(record)
        record["id"] = str(result.inserted_id)
        return ClienteApartado(**record)

    def get_all(self) -> List[ClienteApartado]:
        return [
            ClienteApartado(**{**clienteApartado, "id": str(clienteApartado["_id"])}) 
            for clienteApartado in self.collection.find()
        ]

    def get(self, clienteApartado_id: str) -> Optional[ClienteApartado]:
        clienteApartado = self.collection.find_one({"_id": ObjectId(clienteApartado_id)})
        if clienteApartado:
            return ClienteApartado(**{**clienteApartado, "id": str(clienteApartado["_id"])})
        return None

    def update(self, clienteApartado_id: str, clienteApartado: ClienteApartado) -> bool:
        result = self.collection.update_one(
            {"_id": ObjectId(clienteApartado_id)}, 
            {"$set": clienteApartado.dict(exclude_unset=True)}
        )
        return result.matched_count > 0

    def delete(self, clienteApartado_id: str) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(clienteApartado_id)})
        return result.deleted_count > 0
