from routes.route_repository import RouteRepository
from typing import List,Optional
from models import Route,RouteStop
from graph_types import RouteInput,RouteType,StopType
class RouteService():

    def __init__(self):
        self.repository=RouteRepository()

    def route_to_route_type(self,route):
        stops = self.__get_route_stops(route)
        return RouteType(
            id=route.id,
            name=route.name or "",
            start = stops[0],
            end = stops[-1],
            stops=stops
        )

    def route_input_to_route(self,route_inp):
        return Route(
            name=route_inp.name,
            stops= [RouteStop(stop_id=stop_id, order=i) for i,stop_id in enumerate(route_inp.stop_ids)],
            # stops = [RouteStop(stop_id=route_inp.stops[i].id, order=i)for i in range(len(route_inp.stops))]
        )

        
    def create_route(self,route_inp:RouteInput)-> RouteType:
        route = self.route_input_to_route(route_inp)
        new_route = self.repository.create_route(route)
        
        #kost а оно мне вообзе надо объект туда возвращать?
        return RouteType(
            id=new_route.id,
            name =route_inp.name,
            # start =route_inp.stops[0],
            # end = route_inp.stops[-1],
            # stops = route_inp.stops,
            start = StopType(id=1,name="123"),
            end = StopType(id=1,name="123"),
            stops = [StopType(id=1,name="123")],

        )
    
    def __get_route_stops(self,route):
        return [route_stop.stop for route_stop in sorted(route.stops, key=lambda stop: stop.order)]
        

    def get_route(self,id:int) -> Optional[RouteType]:
        route = self.repository.get_route(id)
        if route:
            return self.route_to_route_type(route)
        return None
    
    def get_all_routes(self)->List[RouteType]:
        routes = self.repository.get_all_routes()
        return [self.route_to_route_type(route) for route in routes]
