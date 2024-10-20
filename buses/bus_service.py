from buses.bus_repository import BusRepository
from typing import List
from buses.types import *

class BusService():

    def __init__(self): 
        self.repository=BusRepository()
        
    def create_bus(self,name:str,schedule_id:int)->BusType:
        new_bus = self.repository.create_bus(name, schedule_id)
        #Kost
        return BusType(id=new_bus.id, name=new_bus.name,schedule_id=schedule_id)
        
    def get_bus(self,id:int)->BusType:
        bus = self.repository.get_bus(id)
        if bus:
            return BusType(id=bus.id, name=bus.name,schedule_id=bus.schedule_id)
        return None
    
    def get_all_buses(self)->List[BusType]:
        buses = self.repository.get_all_buses()

        return [
            BusType(
                id=bus.id,
                name=bus.name,
                schedule_id=bus.schedule_id
            )
            for bus in buses
        ]

