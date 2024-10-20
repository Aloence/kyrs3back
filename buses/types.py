import strawberry



@strawberry.type
class BusType:
    id: int
    name: str
    schedule_id:int