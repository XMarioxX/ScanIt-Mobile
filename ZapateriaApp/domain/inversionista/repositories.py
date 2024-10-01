from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from ZapateriaApp.domain.inversionista.models import Inversionista
from ZapateriaApp.domain.inversionista.repositories import InversionistaRepository

class MongoInversionistaRepository(InversionistaRepository):
    def __init__(self, db):
        self.collection = db.inversionista_collection

    def add(self, inversionista: Inversionista) -> Inversionista:
        record = inversionista.dict(exclude_unset=True)
        result = self.collection.insert_one(record)
        record["id"] = str(result.inserted_id)
        return Inversionista(**record)

    def get_all(self) -> List[Inversionista]:
        return [Inversionista(**{**inversionista, "id": str(inversionista["_id"])}) for inversionista in self.collection.find()]

    def get(self, inversionista_id: str) -> Optional[Inversionista]:
        inversionista = self.collection.find_one({"_id": ObjectId(inversionista_id)})
        if inversionista:
            return Inversionista(**{**inversionista, "id": str(inversionista["_id"])})
        return None

    def update(self, inversionista_id: str, inversionista: Inversionista) -> bool:
        inversionista.fechaUpdate = datetime.now().isoformat()  
        result = self.collection.update_one(
            {"_id": ObjectId(inversionista_id)}, {"$set": inversionista.dict(exclude_unset=True)}
        )
        return result.matched_count > 0

    def delete(self, inversionista_id: str) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(inversionista_id)})
        return result.deleted_count > 0
