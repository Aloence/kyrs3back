from schedules.schedule_repository import ScheduleRepository
from typing import List,Optional
from schedules.types import *

class ScheduleService():

    def __init__(self):
        self.repository=ScheduleRepository()

    def create_schedule(self,route_id:int, stops:List[ScheduleStopInput])-> ScheduleType:

        new_schedule = self.repository.create_schedule(route_id, stops)
        
        #kost
        return ScheduleType(
            id=new_schedule.id,
            route_id=route_id,
            schedule=stops
        )

    
    #надо сделать чтобы остановки в нужном порядке возвращались
    def get_schedule(self,id:int) -> Optional[ScheduleType]:

        schedule = self.repository.get_schedule(id)

        if schedule:
            return ScheduleType(
                id = schedule.id,
                route_id=schedule.route_id,
                schedule=[sch_stop.stop for sch_stop in schedule.schedule_stops]
            )
        return None
    
    def get_all_schedules(self) -> List[ScheduleType]:
        schedules = self.repository.get_all_schedules()
        
        return [
            ScheduleType(
                id = schedule.id,
                route_id=schedule.route_id,
                schedule=[sch_stop.stop for sch_stop in schedule.schedule_stops]
            )
            for schedule in schedules
        ]
    
