import strawberry
from typing import List,Optional
from buses.bus_service import BusService
from graph_types import BusInput,BusType

#kost DI init ?
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
        # print(bus)
        return bus
    

