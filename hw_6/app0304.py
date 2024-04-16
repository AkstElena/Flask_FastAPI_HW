"""
Задание №3
📌 Создать API для управления списком задач.
📌 Каждая задача должна содержать поля "название", "описание" и "статус" (выполнена/не выполнена).
📌 API должен позволять выполнять CRUD операции с задачами.
Задание №4
📌 Напишите API для управления списком задач. Для этого создайте модель Task со следующими полями:
○ id: int (первичный ключ)
○ title: str (название задачи)
○ description: str (описание задачи)
○ done: bool (статус выполнения задачи)
"""
from typing import List
import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel, Field

DATABASE_URL = "sqlite:///database_hw0304.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

tasks = sqlalchemy.Table(
    "tasks",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String(50)),
    sqlalchemy.Column("description", sqlalchemy.String(200)),
    sqlalchemy.Column("done", sqlalchemy.Boolean()),
)

engine = sqlalchemy.create_engine(DATABASE_URL,
                                  connect_args={"check_same_thread": False})  # второй параметр только для sqlite
metadata.create_all(engine)  # создание таблицы в БД

app = FastAPI()


class TaskIn(BaseModel):
    title: str = Field(..., max_length=50)
    description: str = Field(..., max_length=200)
    done: bool = Field(default=False)


class Task(TaskIn):
    id: int


@app.get("/tasks/", response_model=List[Task])
async def read_tasks():
    query = tasks.select()
    return await database.fetch_all(query)


@app.get("/tasks/{task_id}", response_model=Task)  # показать по id
async def read_task(task_id: int):
    query = tasks.select().where(tasks.c.id == task_id)
    return await database.fetch_one(query)


@app.post("/tasks/", response_model=Task)  # добавление новой задачи
async def create_task(task: TaskIn):  # модель без идентификатора
    query = tasks.insert().values(**task.model_dump())
    last_record_id = await database.execute(query)
    return {**task.dict(), "id": last_record_id}


@app.put("/tasks/{task_id}", response_model=Task)  # обновить информацию о задаче
async def update_task(task_id: int, new_task: TaskIn):
    query = tasks.update().where(tasks.c.id == task_id).values(**new_task.model_dump())
    await database.execute(query)
    return {**new_task.model_dump(), "id": task_id}


@app.delete("/tasks/{task_id}")  # удалить задачу
async def delete_task(task_id: int):
    query = tasks.delete().where(tasks.c.id == task_id)
    await database.execute(query)
    return {'message': 'task deleted'}
