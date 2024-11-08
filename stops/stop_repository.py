
from typing import List
from models import Stop
from database import SessionLocal

class StopRepository:

    def create_stop(self, name: str):
        db = SessionLocal()
        new_stop = Stop(name=name)
        db.add(new_stop)
        db.commit()
        db.refresh(new_stop) 
        db.close()
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
    
    def edit_stop(self, id: int, name: str) -> Stop:
        db = SessionLocal()
        stop = db.query(Stop).filter(Stop.id == id).one()

        stop.name = name 
        db.commit()
        db.refresh(stop) 
        db.close()
        return stop
        
