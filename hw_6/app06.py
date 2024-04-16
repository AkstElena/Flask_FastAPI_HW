"""
Задание №6
📌 Необходимо создать базу данных для интернет-магазина. База данных должна состоять из трех таблиц: товары, заказы и
пользователи. Таблица товары должна содержать информацию о доступных товарах, их описаниях и ценах. Таблица пользователи
должна содержать информацию о зарегистрированных пользователях магазина. Таблица заказы должна содержать информацию о
заказах, сделанных пользователями.
○ Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY), имя, фамилия, адрес электронной почты и
пароль.
○ Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.
○ Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id пользователя (FOREIGN KEY),
id товара (FOREIGN KEY), дата заказа и статус заказа.
📌 Создайте модели pydantic для получения новых данных и возврата существующих в БД для каждой из трёх таблиц
(итого шесть моделей).
📌 Реализуйте CRUD операции для каждой из таблиц через создание маршрутов, REST API (итого 15 маршрутов).
○ Чтение всех
○ Чтение одного
○ Запись
○ Изменение
○ Удаление
"""

from typing import List
import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr, PastDate, field_validator

DATABASE_URL = "sqlite:///database_hw06.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("firstname", sqlalchemy.String(30)),
    sqlalchemy.Column("lastname", sqlalchemy.String(30)),
    sqlalchemy.Column("email", sqlalchemy.String(50)),
    sqlalchemy.Column("password", sqlalchemy.String(20)),
)

products = sqlalchemy.Table(
    "products",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(50)),
    sqlalchemy.Column("description", sqlalchemy.String(200)),
    sqlalchemy.Column("price", sqlalchemy.Float()),
)

orders = sqlalchemy.Table(
    "orders",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("id_user", sqlalchemy.Integer, sqlalchemy.ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("id_product", sqlalchemy.Integer, sqlalchemy.ForeignKey(products.c.id), nullable=False),
    sqlalchemy.Column("date", sqlalchemy.Date()),
    sqlalchemy.Column("status", sqlalchemy.String(20)),
)

engine = sqlalchemy.create_engine(DATABASE_URL,
                                  connect_args={"check_same_thread": False})  # второй параметр только для sqlite
metadata.create_all(engine)  # создание таблицы в БД

app = FastAPI()


class UserIn(BaseModel):
    firstname: str = Field(..., max_length=30)
    lastname: str = Field(..., max_length=30)
    email: EmailStr = Field(..., max_length=50)
    password: str = Field(..., min_length=6, max_length=20)

    class Config:
        from_attributes = True


class User(UserIn):
    id: int


class ProductIn(BaseModel):
    name: str = Field(..., max_length=50, unique=True)
    description: str = Field(..., max_length=200)
    price: float = Field(...)

    class Config:
        orm_mode = True

    @field_validator('price')
    def validate_price(cls, value):
        if value <= 0:
            raise ValueError("Price must be a positive number")
        return value


class Product(ProductIn):
    id: int


class OrderIn(BaseModel):
    id_user: int = User
    id_product: int = Product
    date: PastDate
    status: str = Field(..., max_length=50)

    class Config:
        orm_mode = True


class Order(OrderIn):
    id: int


@app.get("/users/", response_model=List[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


@app.get("/users/{user_id}", response_model=User)
async def read_task(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@app.post("/users/", response_model=User)
async def create_task(user: UserIn):
    query = users.insert().values(**user.model_dump())
    last_record_id = await database.execute(query)
    return {**user.model_dump(), "id": last_record_id}


@app.put("/users/{task_id}", response_model=User)
async def update_task(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.model_dump())
    await database.execute(query)
    return {**new_user.model_dump(), "id": user_id}


@app.delete("/users/{user_id}")
async def delete_task(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': 'user deleted'}


@app.get("/products/", response_model=List[Product])
async def read_products():
    query = products.select()
    return await database.fetch_all(query)


@app.get("/products/{product_id}", response_model=Product)
async def read_product(product_id: int):
    query = products.select().where(products.c.id == product_id)
    return await database.fetch_one(query)


@app.post("/products/", response_model=Product)
async def create_product(product: ProductIn):
    query = products.insert().values(**product.model_dump())
    last_record_id = await database.execute(query)
    return {**product.model_dump(), "id": last_record_id}


@app.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: int, new_product: ProductIn):
    query = products.update().where(products.c.id == product_id).values(**new_product.model_dump())
    await database.execute(query)
    return {**new_product.model_dump(), "id": product_id}


@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    query = products.delete().where(products.c.id == product_id)
    await database.execute(query)
    return {'message': 'product deleted'}


@app.get("/orders/", response_model=List[Order])
async def read_orders():
    query = orders.select()
    # query = orders.select().join(users)
    return await database.fetch_all(query)


@app.get("/orders/{order_id}", response_model=Order)
async def read_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)  #.join(products, products.c.id == orders.c.id_user)
    return await database.fetch_one(query)


@app.post("/orders/", response_model=Order)
async def create_order(order: OrderIn):
    query = orders.insert().values(**order.model_dump())
    last_record_id = await database.execute(query)
    return {**order.model_dump(), "id": last_record_id}


@app.put("/orders/{order_id}", response_model=Order)
async def update_order(order_id: int, new_order: OrderIn):
    query = orders.update().where(orders.c.id == order_id).values(**new_order.model_dump())
    await database.execute(query)
    return {**new_order.model_dump(), "id": order_id}


@app.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    return {'message': 'order deleted'}
