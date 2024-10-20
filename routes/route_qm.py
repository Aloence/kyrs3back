import strawberry
from typing import List,Optional
from models import Stop, Route, RouteStop
from database import SessionLocal
from sqlalchemy.orm import Session,joinedload
from routes.route_service import RouteService
from routes.types import *

#kost
route_service = RouteService()

@strawberry.type
class RouteMutation:
    @strawberry.mutation
    def create_route(self, stops: List[StopInput]) -> RouteType:
        route = route_service.create_route(stops)
        return route

    
@strawberry.type
class RouteQuery:
    @strawberry.field
    def all_routes(self) -> List[RouteType]:
        routes = route_service.get_all_routes()
        return routes

    @strawberry.field
    def route_by_id(self, route_id: int) -> Optional[RouteType]:
        route = route_service.get_route(route_id)
        return route

