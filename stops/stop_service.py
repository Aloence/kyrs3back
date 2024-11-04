from stops.stop_repository import StopRepository
from typing import List
from stops.types import *


class StopService():

    def __init__(self):
        self.repository=StopRepository()
        
    def create_stop(self,stop_input)->StopType:
                                                    #kost--|
        new_stop = self.repository.create_stop(stop_input.name)
        
        return StopType(id=new_stop.id, name=new_stop.name)
        
    def get_stop(self,id:int)->StopType:
        stop = self.repository.get_stop(id)
        if stop:
            return StopType(id=stop.id, name=stop.name)
        return None
    
    def get_all_stops(self)->List[StopType]:
        stops = self.repository.get_all_stops()

        return [
            StopType(
                id=stop.id,
                name=stop.name
            )
            for stop in stops
        ]

    def edit_stop(self, id, stop_input):
        #kost
        edited_stop = self.repository.edit_stop(id,stop_input.name)
        if edited_stop: 
            return edited_stop
        return None
    
    # def delete_stop(id):
    #     pass
