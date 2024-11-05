import strawberry
from typing import List,Optional
from routes.route_service import RouteService
from graph_types import RouteInput,RouteType

#kost DI init ?
route_service = RouteService()

@strawberry.type
class RouteMutation:
    @strawberry.mutation
    def create_route(self, route_input:RouteInput) -> RouteType:
        route = route_service.create_route(route_input)
        return route

    
@strawberry.type
class RouteQuery:
    @strawberry.field
    def get_routes(self) -> List[RouteType]:
        routes = route_service.get_all_routes()
        return routes

    @strawberry.field
    def get_route_by_id(self, route_id: int) -> Optional[RouteType]:
        route = route_service.get_route(route_id)
        return route

