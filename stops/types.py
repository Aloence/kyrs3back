import strawberry

@strawberry.input
class StopInput:
    id:int
    name:str

@strawberry.type
class StopType:
    id: int
    name: str