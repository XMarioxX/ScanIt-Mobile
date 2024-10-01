from bson import ObjectId
from pymongo import MongoClient
from typing import List, Optional
from ZapateriaApp.domain.proveedor.models import Proveedor
from ZapateriaApp.domain.proveedor.repositories import ProveedorRepository

class MongoProveedorRepository(ProveedorRepository):
    def __init__(self, db: MongoClient):
        self.collection = db.proveedor_collection

    def add(self, proveedor: Proveedor) -> Proveedor:
        record = proveedor.dict(exclude_unset=True)
        result = self.collection.insert_one(record)
        record["id"] = str(result.inserted_id)
        return Proveedor(**record)

    def get_all(self) -> List[Proveedor]:
        return [
            Proveedor(**{**proveedor, "id": str(proveedor["_id"])}) 
            for proveedor in self.collection.find()
        ]

    def get(self, proveedor_id: str) -> Optional[Proveedor]:
        proveedor = self.collection.find_one({"_id": ObjectId(proveedor_id)})
        if proveedor:
            return Proveedor(**{**proveedor, "id": str(proveedor["_id"])})
        return None

    def update(self, proveedor_id: str, proveedor: Proveedor) -> bool:
        result = self.collection.update_one(
            {"_id": ObjectId(proveedor_id)}, 
            {"$set": proveedor.dict(exclude_unset=True)}
        )
        return result.matched_count > 0

    def delete(self, proveedor_id: str) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(proveedor_id)})
        return result.deleted_count > 0
