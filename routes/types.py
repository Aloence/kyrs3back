import strawberry
from typing import List


@strawberry.input
class StopInput:
    id:int
    name:str


@strawberry.type
class StopType:
    id: int
    name: str


@strawberry.type
class RouteType:
    id: int
    stops: List[StopType]
