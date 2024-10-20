from sqlalchemy.orm import Session,joinedload
from database import SessionLocal
from typing import List
from models import Stop, Route, RouteStop

class RouteRepository:
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

