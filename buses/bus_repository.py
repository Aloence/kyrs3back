from sqlalchemy.orm import Session,joinedload
from typing import List
from models import Bus
from database import SessionLocal

class BusRepository:

    def create_bus(self, name: str,schedule_id:int):
        db = SessionLocal()
        new_bus = Bus(name=name,schedule_id=schedule_id)
        db.add(new_bus)
        db.commit()
        db.refresh(new_bus)  # Получаем обновленные данные о новой остановке
        db.close()
        
        return new_bus

    def get_all_buses(self)->List[Bus]:
        db = SessionLocal()
        buses = db.query(Bus).all()
        db.close()
        return buses
    
    def get_bus(self,id:int)->Bus:
        db = SessionLocal()
        bus = db.query(Bus).filter(Bus.id == id).one()
        db.close()
        return bus
