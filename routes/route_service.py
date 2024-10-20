from routes.route_repository import RouteRepository
from typing import List,Optional
from routes.types import *
class RouteService():

    def __init__(self):
        self.repository=RouteRepository()

    #???
    def create_route(self,stops:List[StopInput])-> RouteType:

        new_route = self.repository.create_route(stops)
        
        #kost
        return RouteType(
            id=new_route.id,
            stops=[StopType(id=stop.id, name=stop.name) for stop in stops]
        )
    #??
    # def __StopInputToStop(self,stpinp:StopInput):
    #     return 
    # def routetypetoroute и наоборот
    def __get_route_stops(self,route):
        return [route_stop.stop for route_stop in sorted(route.stops, key=lambda stop: stop.order)]
        

    def get_route(self,id:int) -> Optional[RouteType]:
        route = self.repository.get_route(id)
    
        if route:
            return RouteType(
                id=route.id,
                stops=self.__get_route_stops(route)
            )
        return None
    
    def get_all_routes(self)->List[RouteType]:
        routes = self.repository.get_all_routes()
        
        return [
            RouteType(
                id=route.id,
                stops=self.__get_route_stops(route)
            )
            for route in routes
        ]
    
