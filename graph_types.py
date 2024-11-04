import strawberry
from typing import List


@strawberry.type
class StopType:
    id: int
    name: str

@strawberry.type
class RouteType:
    id: int
    name:str
    stops: List[StopType]
    start:StopType
    end:StopType


@strawberry.type
class ScheduleStopType:
    id:int
    stop:StopType
    time:str

@strawberry.type
class ScheduleType:
    id: int
    name:str
    route: RouteType
    start:str
    end:str
    schedule:List[ScheduleStopType]
    #+schedule

# @strawberry.type
# class ScheduleStopType:
#     id:int
#     name:str
#     time:str

@strawberry.type
class BusType:
    id: int
    name: str
    price:float 
    schedule:ScheduleType



@strawberry.input
class StopInput:
    name:str # как будто не надо вообще 


@strawberry.input
class RouteInput:
    name:str
    stop_ids:List[int]

@strawberry.input
class ScheduleStopInput:
    stop_id:int
    time:str

@strawberry.input
class ScheduleInput:
    name:str
    start:str
    end:str
    route_id:int
    schedule:List[ScheduleStopInput]

@strawberry.input
class BusInput:
    price:int
    name:str
    schedule_id:int





