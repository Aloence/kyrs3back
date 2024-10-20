import strawberry
from typing import List,Optional
from models import Stop, Route, RouteStop
from database import SessionLocal
from sqlalchemy.orm import Session,joinedload
from stops.stop_service import StopService
from stops.types import *


stop_service = StopService()
@strawberry.type
class StopMutation:
    @strawberry.mutation
    def create_stop(self, name: str) -> StopType:
        new_stop = stop_service.create_stop(name)
        return new_stop


@strawberry.type
class StopQuery:
    @strawberry.field
    def all_stops(self) -> List[StopType]:
        stops = stop_service.get_all_stops()
        return stops

    
    @strawberry.field
    def stop_by_id(self, stop_id: int) -> Optional[StopType]:
        stop = stop_service.get_stop(stop_id)
        return stop
    

