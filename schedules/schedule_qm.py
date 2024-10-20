import strawberry
from typing import List,Optional
from models import Stop, Route, RouteStop
from database import SessionLocal
from sqlalchemy.orm import Session,joinedload
from schedules.types import *
from schedules.schedule_service import ScheduleService


schedule_service = ScheduleService()
@strawberry.type
class ScheduleMutation:
    @strawberry.mutation
    def create_schedule(self, route_id:int,schedule: List[ScheduleStopInput]) -> ScheduleType:
        schedule = schedule_service.create_schedule(route_id, schedule)
        return schedule

@strawberry.type
class ScheduleQuery:
    @strawberry.field
    def all_schedules(self) -> List[ScheduleType]:
        schedules = schedule_service.get_all_schedules()
        return schedules

    @strawberry.field
    def schedule_by_id(self, schedule_id: int) -> Optional[ScheduleType]:
        schedule = schedule_service.get_schedule(schedule_id)
        return schedule
    
