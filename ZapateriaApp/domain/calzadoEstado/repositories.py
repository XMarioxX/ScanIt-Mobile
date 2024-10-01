from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from ZapateriaApp.domain.calzadoEstado.models import CalzadoEstado
from ZapateriaApp.domain.calzadoEstado.repositories import CalzadoEstadoRepository

class MongoCalzadoEstadoRepository(CalzadoEstadoRepository):
    def __init__(self, db):
        self.collection = db.calzadoEstado_collection

    def add(self, calzadoEstado: CalzadoEstado) -> CalzadoEstado:
        record = calzadoEstado.dict(exclude_unset=True)
        result = self.collection.insert_one(record)
        record["id"] = str(result.inserted_id)
        return CalzadoEstado(**record)

    def get_all(self) -> List[CalzadoEstado]:
        return [CalzadoEstado(**{**calzadoEstado, "id": str(calzadoEstado["_id"])}) for calzadoEstado in self.collection.find()]

    def get(self, calzadoEstado_id: str) -> Optional[CalzadoEstado]:
        calzadoEstado = self.collection.find_one({"_id": ObjectId(calzadoEstado_id)})
        if calzadoEstado:
            return CalzadoEstado(**{**calzadoEstado, "id": str(calzadoEstado["_id"])})
        return None

    def update(self, calzadoEstado_id: str, calzadoEstado: CalzadoEstado) -> bool:
        calzadoEstado.fechaUpdate = datetime.now().isoformat()  
        result = self.collection.update_one(
            {"_id": ObjectId(calzadoEstado_id)}, {"$set": calzadoEstado.dict(exclude_unset=True)}
        )
        return result.matched_count > 0

    def delete(self, calzadoEstado_id: str) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(calzadoEstado_id)})
        return result.deleted_count > 0
