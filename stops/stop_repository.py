from sqlalchemy.orm import Session,joinedload
from typing import List
from models import Stop
from database import SessionLocal

class StopRepository:

    def create_stop(self, name: str):
        db = SessionLocal()
        new_stop = Stop(name=name)
        db.add(new_stop)
        db.commit()
        db.refresh(new_stop)  # Получаем обновленные данные о новой остановке
        db.close()
        print(new_stop.name,new_stop.id,)
        return new_stop

    def get_all_stops(self)->List[Stop]:
        db = SessionLocal()
        stops = db.query(Stop).all()
        db.close()
        return stops
    
    def get_stop(self,id:int)->Stop:
        db = SessionLocal()
        stop = db.query(Stop).filter(Stop.id == id).one()
        db.close()
        return stop
