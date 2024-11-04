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
    def create_stop(self, stop_input:StopInput) -> StopType:
        new_stop = stop_service.create_stop(stop_input)
        return new_stop
    
    @strawberry.mutation
    def edit_stop(self, stop_id:int, stop_input:StopInput)->StopType:
        edited_stop = stop_service.edit_stop(stop_id,stop_input)
        return edited_stop
    # def delete_stop(self,stop_id:int)-> bool:
    #     stoo_deleted = stop_service.delete_stop(stop_id)
    #     return stoo_deleted

@strawberry.type
class StopQuery:
    @strawberry.field
    def get_stops(self) -> List[StopType]:
        print('da')
        stops = stop_service.get_all_stops()
        return stops

    
    @strawberry.field
    def get_stop_by_id(self, stop_id: int) -> Optional[StopType]:
        stop = stop_service.get_stop(stop_id)
        return stop
    

