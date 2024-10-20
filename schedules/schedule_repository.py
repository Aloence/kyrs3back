from sqlalchemy.orm import Session,joinedload
from database import SessionLocal
from typing import List, Optional
from models import Stop, Route, RouteStop, Schedule, ScheduleStop

class ScheduleRepository:
    def create_schedule(self, route_id: int, schedule_stops: list)->Schedule:
        db = SessionLocal()
        schedule = Schedule(route_id=route_id)
        db.add(schedule)
        db.flush()  # Чтобы получить ID маршрута

        for order, sch_stop in enumerate(schedule_stops):
            schedule_stop = ScheduleStop(schedule_id=schedule.id,stop_id=sch_stop.id,time=sch_stop.time,order=order)
            # schedule.schedule_stops.append(schedule_stop)
            db.add(schedule_stop)

        db.commit()
        db.refresh(schedule)
        db.close()
        return schedule
    
    def get_all_schedules(self)->List[Schedule]:
        db = SessionLocal()
        schedules = db.query(Schedule).options(
            joinedload(Schedule.schedule_stops).joinedload(ScheduleStop.stop)
        ).all()

        db.close()
        return schedules

    def get_schedule(self, id:int)->Optional[Schedule]:
        db = SessionLocal()
        schedule = db.query(Schedule).options(
            joinedload(Schedule.schedule_stops).joinedload(ScheduleStop.stop)
        ).filter(Schedule.id == id).one()
        
        db.close()
        return schedule
