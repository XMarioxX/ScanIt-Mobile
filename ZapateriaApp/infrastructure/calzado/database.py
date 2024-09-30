from bson import ObjectId
from pymongo import MongoClient
from typing import List, Optional
from ZapateriaApp.domain.calzado.models import Calzado
from ZapateriaApp.domain.calzado.repositories import CalzadoRepository

class MongoCalzadoRepository(CalzadoRepository):
    def __init__(self, db: MongoClient):
        self.collection = db.calzado_collection

    def add(self, calzado: Calzado) -> Calzado:
        record = calzado.dict(exclude_unset=True)
        result = self.collection.insert_one(record)
        record["id"] = str(result.inserted_id)
        return Calzado(**record)

    def get_all(self) -> List[Calzado]:
        return [
            Calzado(**{**calzado, "id": str(calzado["_id"])}) 
            for calzado in self.collection.find()
        ]

    def get(self, calzado_id: str) -> Optional[Calzado]:
        calzado = self.collection.find_one({"_id": ObjectId(calzado_id)})
        if calzado:
            return Calzado(**{**calzado, "id": str(calzado["_id"])})
        return None

    def update(self, calzado_id: str, calzado: Calzado) -> bool:
        result = self.collection.update_one(
            {"_id": ObjectId(calzado_id)}, 
            {"$set": calzado.dict(exclude_unset=True)}
        )
        return result.matched_count > 0

    def delete(self, calzado_id: str) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(calzado_id)})
        return result.deleted_count > 0
