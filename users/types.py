import strawberry

@strawberry.input
class StopInput:
    id:int
    name:str

@strawberry.type
class UserType:
    login: int
    password: str

@strawberry.type
class UserInfoType:
    balance: int
    name: str
    