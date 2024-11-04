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
    def create_schedule(self, schedule_input:ScheduleInput) -> ScheduleType:
        print(schedule_input)
        schedule = schedule_service.create_schedule(schedule_input)
        return schedule

@strawberry.type
class ScheduleQuery:
    @strawberry.field
    def get_schedules(self) -> List[ScheduleType]:
        schedules = schedule_service.get_all_schedules()
        return schedules

    @strawberry.field
    def get_schedule_by_id(self, schedule_id: int) -> Optional[ScheduleType]:
        schedule = schedule_service.get_schedule(schedule_id)
        return schedule
    
