from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from schema import schema
from database import engine, Base

# Создаем все таблицы
Base.metadata.create_all(bind=engine)

app = FastAPI()

graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")