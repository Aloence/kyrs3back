import strawberry
from typing import List,Optional
from models import User, Route, RouteUser
from database import SessionLocal
from sqlalchemy.orm import Session,joinedload
from users.user_service import UserService
from users.types import *


user_service = UserService()
@strawberry.type
class UserMutation:
    @strawberry.mutation
    def registation(self, login: str, password:str) -> bool:
        new_user = user_service.registration(login, password)
        return new_user.role
    

    #мб эти 2 можно объединить
    @strawberry.mutation
    def create_user_info(self, user_id: str, name:str) -> UserInfoType:
        new_user = user_service.create_user_info(user_id, name)
        return new_user
    
    @strawberry.mutation
    def change_balance(self, user_id: int) -> UserInfoType:
        new_user = user_service.change_balance(user_id)
        return new_user


@strawberry.type
class UserQuery:
    @strawberry.field
    def login(self,login,password) -> bool:
        user = user_service.login(login,password)
        return user.role

    
    @strawberry.field
    def user_info(self, user_id: int) -> UserInfoType:
        user_info = user_service.get_user_info(user_id)
        return user_info
    

