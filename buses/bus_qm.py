import strawberry
from typing import List,Optional
from models import  Route, Bus
from database import SessionLocal
from sqlalchemy.orm import Session,joinedload
from buses.bus_service import BusService
from buses.types import *


bus_service = BusService()
@strawberry.type
class BusMutation:
    @strawberry.mutation
    def create_bus(self, bus_input:BusInput) -> BusType:
        new_bus = bus_service.create_bus(bus_input)
        return new_bus


@strawberry.type
class BusQuery:
    @strawberry.field
    def get_buses(self) -> List[BusType]:
        buses = bus_service.get_all_buses()
        return buses

    
    @strawberry.field
    def get_bus_by_id(self, bus_id: int) -> Optional[BusType]:
        bus = bus_service.get_bus(bus_id)
        print(bus)
        return bus
    

