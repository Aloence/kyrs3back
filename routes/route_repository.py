from sqlalchemy.orm import Session,joinedload
from database import SessionLocal
from typing import List
from models import Stop, Route, RouteStop

class RouteRepository:
    def create_route(self, route:Route)->Route:
        db = SessionLocal()
        db.add(route)
        db.commit()
        
        db.refresh(route)
        # db.refresh(route,attribute_names=["stops"])

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

