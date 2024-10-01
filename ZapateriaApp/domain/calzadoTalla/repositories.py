from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from ZapateriaApp.domain.calzadoTalla.models import CalzadoTalla
from ZapateriaApp.domain.calzadoTalla.repositories import CalzadoTallaRepository

class MongoCalzadoTallaRepository(CalzadoTallaRepository):
    def __init__(self, db):
        self.collection = db.calzadoTalla_collection

    def add(self, calzadoTalla: CalzadoTalla) -> CalzadoTalla:
        record = calzadoTalla.dict(exclude_unset=True)
        result = self.collection.insert_one(record)
        record["id"] = str(result.inserted_id)
        return CalzadoTalla(**record)

    def get_all(self) -> List[CalzadoTalla]:
        return [CalzadoTalla(**{**calzadoTalla, "id": str(calzadoTalla["_id"])}) for calzadoTalla in self.collection.find()]

    def get(self, calzadoTalla_id: str) -> Optional[CalzadoTalla]:
        calzadoTalla = self.collection.find_one({"_id": ObjectId(calzadoTalla_id)})
        if calzadoTalla:
            return CalzadoTalla(**{**calzadoTalla, "id": str(calzadoTalla["_id"])})
        return None

    def update(self, calzadoTalla_id: str, calzadoTalla: CalzadoTalla) -> bool:
        calzadoTalla.fechaUpdate = datetime.now().isoformat()  
        result = self.collection.update_one(
            {"_id": ObjectId(calzadoTalla_id)}, {"$set": calzadoTalla.dict(exclude_unset=True)}
        )
        return result.matched_count > 0

    def delete(self, calzadoTalla_id: str) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(calzadoTalla_id)})
        return result.deleted_count > 0
