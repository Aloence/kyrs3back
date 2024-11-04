from schedules.schedule_repository import ScheduleRepository
from typing import List,Optional
from models import *
from schedules.types import *

class ScheduleService():

    def __init__(self):
        self.repository=ScheduleRepository()

    def create_schedule(self,schedule_inp)-> ScheduleType:
        schedule=self.schedule_input_to_schedule(schedule_inp)
        new_schedule = self.repository.create_schedule(schedule)
        #kost
        return ScheduleType(
            id=new_schedule.id,
            name=new_schedule.name,
            start=new_schedule.start,
            end=new_schedule.end,
            route=None,
            schedule=None,
        )

    
    #надо сделать чтобы остановки в нужном порядке возвращались
    def get_schedule(self,id:int) -> Optional[ScheduleType]:
        schedule = self.repository.get_schedule(id)
        if schedule:
            return self.schedule_to_schedule_type(schedule)
        return None
  
    def get_all_schedules(self) -> List[ScheduleType]:
        schedules = self.repository.get_all_schedules()
        return [self.schedule_to_schedule_type(schedule) for schedule in schedules]
        
    def schedule_input_to_schedule(self,schedule_inp:ScheduleInput):
        return Schedule(
            route_id=schedule_inp.route_id,
            name=schedule_inp.name,
            start=schedule_inp.start,
            end = schedule_inp.end,
            schedule_stops = [ScheduleStop(
                stop_id=schedule_stop.stop_id,
                time = schedule_stop.time,
                order=i,
                )for i,schedule_stop in enumerate(schedule_inp.schedule)]
        )
    

    def schedule_to_schedule_type(self,schedule:Schedule): 

        stops = self.__get_route_stops(schedule.route)
        return ScheduleType(
            id=schedule.id,
            name=schedule.name,
            start=schedule.start,
            end=schedule.end,
            route=RouteType(
                id=schedule.route.id,
                stops = stops,
                start=stops[0],
                end=stops[-1],
                name=schedule.route.name,
            ),
            schedule=[
                ScheduleStopType(
                    id=schedule_stop.id,
                    stop=schedule_stop.stop,
                    time=schedule_stop.time,
                )
            for schedule_stop in schedule.schedule_stops]
        )
    
    #pozor
    def __get_route_stops(self,route):
        return [route_stop.stop for route_stop in sorted(route.stops, key=lambda stop: stop.order)]
  
