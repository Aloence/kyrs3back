from sqlalchemy.orm import joinedload
from typing import List
from models import Bus,Schedule,Route,ScheduleStop,RouteStop
from database import SessionLocal

class BusRepository:

    def create_bus(self, bus:Bus):
        db = SessionLocal()
        db.add(bus)
        db.commit()
        db.refresh(bus) 
        db.close()
        
        return bus

    def get_all_buses(self)->List[Bus]:
        db = SessionLocal()
        buses = db.query(Bus).options(
            joinedload(Bus.schedule).options(
            joinedload(Schedule.route).joinedload(Route.stops).joinedload(RouteStop.stop),
            joinedload(Schedule.schedule_stops).joinedload(ScheduleStop.stop)
            )
        ).all()

        buses = db.query(Bus).all()
        db.close()
        return buses
    
    def get_bus(self,id:int)->Bus:
        db = SessionLocal()
        bus = db.query(Bus).options(
            joinedload(Bus.schedule).options(
            joinedload(Schedule.route).joinedload(Route.stops).joinedload(RouteStop.stop),
            joinedload(Schedule.schedule_stops).joinedload(ScheduleStop.stop)
            )
        ).filter(Bus.id == id).one()
        db.close()
        return bus
