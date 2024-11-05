from sqlalchemy.orm import joinedload
from database import SessionLocal
from typing import List, Optional
from models import  Route, RouteStop, Schedule, ScheduleStop

class ScheduleRepository:
    def create_schedule(self, schedule)->Schedule:
        db = SessionLocal()
        db.add(schedule)
        
        db.commit()
        db.refresh(schedule)
        db.close()
        return schedule
    
    def get_all_schedules(self)->List[Schedule]:
        db = SessionLocal()
        schedules = db.query(Schedule).options(
            joinedload(Schedule.route).joinedload(Route.stops).joinedload(RouteStop.stop),
            # 
            joinedload(Schedule.schedule_stops).joinedload(ScheduleStop.stop)
        ).all()
        # for s in schedules:
        #     # print(s)
        #     print(s.route.start)
        db.close()
        return schedules

    def get_schedule(self, id:int)->Optional[Schedule]:
        db = SessionLocal()
        schedule = db.query(Schedule).options(
            joinedload(Schedule.route).joinedload(Route.stops).joinedload(RouteStop.stop),
            joinedload(Schedule.schedule_stops).joinedload(ScheduleStop.stop)
        ).filter(Schedule.id==id).one()
        
        db.close()
        return schedule
