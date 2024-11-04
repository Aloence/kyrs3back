from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter
from schema import schema
from database import engine, Base

# Создаем все таблицы
Base.metadata.create_all(bind=engine)

app = FastAPI()

# graphql_app = GraphQLRouter(schema)
# app.include_router(graphql_app, prefix="/graphql")

# Настройка CORS
origins = [
    "http://localhost:3000",  # Замените на адрес вашего клиента
    "http://127.0.0.1:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Укажите разрешенные источники
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы
    allow_headers=["*"],  # Разрешить все заголовки
)

# Добавьте маршрут для GraphQL
app.include_router(GraphQLRouter(schema), prefix="/graphql")

# Запустите приложение
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)