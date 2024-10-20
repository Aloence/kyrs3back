import strawberry
from typing import List


@strawberry.type
class StopType:
    id: int
    name: str

@strawberry.input
class ScheduleStopInput:
    id:int
    time:str

@strawberry.type
class ScheduleStopType:
    id:int
    name:str
    time:str

@strawberry.type
class ScheduleType:
    id: int
    route_id: int
    schedule: List[ScheduleStopType]

@strawberry.input
class StopInput:
    id:int
    name:str

@strawberry.input
class ScheduleInput:
    id:int
    name:str
    time:str



# @strawberry.type
# class RouteStopType:
#     id: int
#     route_id: int
#     stop_id: int
#     order: int

@strawberry.type
class RouteType:
    id: int
    stops: List[StopType]


