from buses.bus_repository import BusRepository
from typing import List
from models import *
from buses.types import *

class BusService():

    def __init__(self): 
        self.repository=BusRepository()
        
    def create_bus(self,bus_input)->BusType:
        bus = self.bus_input_to_bus(bus_input)
        new_bus = self.repository.create_bus(bus)

        #Kost
        return BusType(id=new_bus.id, name=new_bus.name,price = 123,schedule=None)
        
    def get_bus(self,id:int)->BusType:
        bus = self.repository.get_bus(id)
        if bus:
            return self.bus_to_bus_type(bus)
        return None

    def get_all_buses(self)->List[BusType]:
        buses = self.repository.get_all_buses()
        return [self.bus_to_bus_type(bus) for bus in buses]
    
    def bus_input_to_bus(self,bus_input:BusInput):
        return Bus(
            name=bus_input.name,
            # price=bus_input.price,
            schedule_id=bus_input.schedule_id,
        )

    def bus_to_bus_type(self,bus:Bus):
        stops = self.__get_route_stops(bus.schedule.route)
        #в адаптер какой нить общий вынести норм как будто
        route = RouteType(
                id=bus.schedule.route.id,
                name = bus.schedule.route.name,
                stops = stops,
                start=stops[0],
                end=stops[-1]
        )
        schedule = ScheduleType(
            id = bus.schedule.id,
            route = route,
            name=bus.schedule.name,
           
            start=bus.schedule.start,
            end = bus.schedule.end,
            # schedule =None,
            schedule=[
                ScheduleStopType(
                    id=schedule_stop.id,
                    stop=schedule_stop.stop,
                    time=schedule_stop.time,
                )
            for schedule_stop in bus.schedule.schedule_stops],
        )
        [print(schedule_stop.stop) for schedule_stop in bus.schedule.schedule_stops]
        
        return BusType(
            id=bus.id,
            name=bus.name,
            schedule=schedule,
            price = 123
        )

    #pozor
    def __get_route_stops(self,route):
        return [route_stop.stop for route_stop in sorted(route.stops, key=lambda stop: stop.order)]
    
    