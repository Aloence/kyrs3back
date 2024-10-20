from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Stop(Base):
    __tablename__ = 'stops'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    routes = relationship("RouteStop", back_populates="stop")

    def __str__(self):
        # [print(route) for route in self.routes]
        return f'{self.id}, {self.name}'

class Route(Base):
    __tablename__ = 'routes'

    id = Column(Integer, primary_key=True, index=True)
    stops = relationship("RouteStop", back_populates="route", cascade="all, delete-orphan")

    def __str__(self):
        s = str(self.id)
        [print(stop) for stop in self.stops]
        # [s.join(str(stop)) for stop in self.stops]
        return s

class RouteStop(Base):
    __tablename__ = 'route_stops'

    id = Column(Integer, primary_key=True, index=True)
    route_id = Column(Integer, ForeignKey('routes.id'))
    stop_id = Column(Integer, ForeignKey('stops.id'))
    order = Column(Integer)

    route = relationship("Route", back_populates="stops")
    stop = relationship("Stop", back_populates="routes")

    def __str__(self):
        return f'id:{self.id},route:{self.route_id},stop:{self.stop_id}'

class Schedule(Base):
    __tablename__ = 'schedules'

    id = Column(Integer, primary_key=True, index=True)
    route_id = Column(Integer, ForeignKey('routes.id'))
    schedule_stops = relationship("ScheduleStop", back_populates="schedule", cascade="all, delete-orphan")
    buses = relationship("Bus", back_populates="schedule", cascade="all, delete-orphan")

class ScheduleStop(Base):
    __tablename__ = 'schedule_stops'

    id = Column(Integer, primary_key=True, index=True)
    stop_id = Column(Integer, ForeignKey('stops.id'))
    schedule_id = Column(Integer, ForeignKey('schedules.id'))
    time = Column(String)
    order = Column(Integer)

    schedule = relationship("Schedule", back_populates="schedule_stops")
    stop = relationship("Stop")

    def __str__(self):
        return f'id:{self.id},stop_id:{self.stop_id},schedule_id:{self.schedule_id},order:{self.order}'
    
class Bus(Base):
    __tablename__ = 'buses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    schedule_id = Column(Integer, ForeignKey('schedules.id'))

    schedule = relationship("Schedule", back_populates="buses")

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, schedule_id: {self.schedule_id}'


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    login = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(Boolean, default=False)

    user_info = relationship("UserInfo", back_populates="user", uselist=False)

class UserInfo(Base):
    __tablename__ = 'user_infos'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(String, nullable=False)
    balance = Column(Integer, default=100)

    user = relationship("User", back_populates="user_info")