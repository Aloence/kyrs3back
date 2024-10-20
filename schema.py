import strawberry
from typing import List
from models import Stop, Route, RouteStop
from database import SessionLocal
from sqlalchemy.orm import Session,joinedload
from stops.stop_qm import StopMutation,StopQuery
from routes.route_qm import RouteMutation,RouteQuery
from schedules.schedule_qm import ScheduleMutation, ScheduleQuery
from buses.bus_qm import BusMutation, BusQuery
from users.user_qm import UserMutation, UserQuery


@strawberry.type
class Mutation(UserMutation):
    pass
@strawberry.type
class Query(UserQuery):
    pass
    

schema = strawberry.Schema(query=Query, mutation=Mutation)