from sqlalchemy.orm import Session,joinedload
from typing import List
from models import User,UserInfo
from database import SessionLocal

class UserRepository:
    def create_user(self,login, password):
        db = SessionLocal()
        new_user = User(login=login,password=password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)  
        db.close()
        return new_user

    
    def get_user(self, login, password):
        db = SessionLocal()
        user = db.query(User).filter(User.login == login).one()
        db.close()
        return user

    
    def create_user_info(self, user_id, name):
        db = SessionLocal()
        new_user_info = UserInfo(user_id=user_id,name=name)
        db.add(new_user_info)
        db.commit()
        db.refresh(new_user_info)  
        db.close()
        return new_user_info

    
    def change_balance(self,user_id, balance):
        db = SessionLocal()
        user_info = db.query(UserInfo).filter(UserInfo.user_id == user_id).one()
        user_info
        db.commit()
        db.refresh(new_user_info)  
        db.close()
        return new_user_info

    
    def get_user_info(self, user_id):
       
        return None
       
    def create_route(self, stops: list)->Route:
        db = SessionLocal()
        route = Route()
        db.add(route)
        db.flush()  # Чтобы получить ID маршрута

        for order, stop in enumerate(stops):
            route_stop = RouteStop(route_id=route.id, stop_id=stop.id, order=order)
            db.add(route_stop)

        db.commit()
        db.refresh(route)
        db.close()
        return route
    
    
    def get_all_routes(self)->List[Route]:
        db = SessionLocal()
        routes = db.query(Route).options(
            joinedload(Route.stops).joinedload(RouteStop.stop)
        ).all()

        db.close()
        return routes
    
    def get_route(self, id:int)->Route:
        db = SessionLocal()
        route = db.query(Route).options(
            joinedload(Route.stops).joinedload(RouteStop.stop)
        ).filter(Route.id == id).one()
        db.close()
        return route
