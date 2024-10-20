from users.user_repository import UserRepository
from typing import List
from users.types import *

class UserService():

    def __init__(self):
        self.repository=UserRepository()
        
    def registration(self,login, password)->UserType:
        new_user = self.repository.create_user(login, password)
        
        return UserType(id=new_user.id, login=new_user.name,role = new_user.role)
    
    def login(self, login, password):
        user = self.repository.get_user(login, password)
        if user:
            return UserType(id=user.id, role=user.role)
        return None
    
    def create_user_info(self, user_id, name):
        new_user_info = self.repository.create_user_info(user_id,name)
        return UserInfoType(balance=new_user_info.balance, name=new_user_info.name)
    
    def change_balance(self,user_id, balance):
        user_info = self.repository.change_balance(user_id,balance)
        if user_info:
            return UserInfoType(balance=user_info.balance, name=user_info.name)
        return None
    
    def get_user_info(self, user_id):
        user_info = self.repository.get_user_info(user_id)
        if user_info:
            return UserInfoType(balance=user_info.balance, name=user_info.name)
        return None
       

