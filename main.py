from fastapi import FastAPI
from uuid import uuid4
from typing import List
from models import Gender, User, Role
app = FastAPI()
db: List[User] = [
    User(
        id=uuid4(),
        first_name="John",
        last_name="Doe",
        gender=Gender.male,
        roles=[Role.user],
    ),
    User(
        id=uuid4(),
        first_name="Jane",
        last_name="Doe",
        gender=Gender.female,
        roles=[Role.user],
    ),
    User(
        id=uuid4(),
        first_name="James",
        last_name="Gabriel",
        gender=Gender.male,
        roles=[Role.user],
    ),
    User(
        id=uuid4(),
        first_name="Eunit",
        last_name="Eunit",
        gender=Gender.male,
        roles=[Role.admin, Role.user],
    ),
]

# main.py
@app.get("/api/v1/users")
async def get_users():
 return db

@app.post("/api/v1/users")
async def create_user(user: User):
 db.append(user)
 return {"id": user.id}