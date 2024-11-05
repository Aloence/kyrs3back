import strawberry
from stops.stop_qm import StopMutation,StopQuery
from routes.route_qm import RouteMutation,RouteQuery
from schedules.schedule_qm import ScheduleMutation, ScheduleQuery
from buses.bus_qm import BusMutation, BusQuery




queries =[StopQuery,RouteQuery,ScheduleQuery,BusQuery]
mutations =[StopMutation,RouteMutation,ScheduleMutation,BusMutation]
num = 3
# @strawberry.type
# class Mutation(mutations[num]):
#     pass
# @strawberry.type
# class Query(queries[num]):
#     pass

@strawberry.type
class Mutation(StopMutation,RouteMutation,ScheduleMutation,BusMutation):
    pass
@strawberry.type
class Query(StopQuery,RouteQuery,ScheduleQuery,BusQuery):
    pass

schema = strawberry.Schema(query=Query, mutation=Mutation)