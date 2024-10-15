#Let's start by creating a basic structure of the API

#import essential modules
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker


try:
    DATABASE_URL = load_dotenv("DATABASE_URL")
    print("database connected")
except:
    print("database couldn't be connected ") 

#creating the asyncronous engine
engine = create_async_engine(DATABASE_URL, echo = True)

#creating session
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit = False 
)
#step 3 : creating the dependency to get the session
async def get_session():
    async with async_session() as session:
        yield session               




app:FastAPI= FastAPI()

class Todo(BaseModel):
    id: int
    title: str 
    description: str
    completed: bool= False

todo_list: List[Todo] = []

@app.get("/")
def read_root():
    return{"message":"welcome to the todo api"}

#endpoint to read all the Todos
@app.get("/todos", response_model=List[Todo])
def get_todos():
    return todo_list

#endpoint to create a Todo 
@app.post("/todos", response_model=Todo)
def create_todo(todo:Todo): #indication that the object of class Todo should be passed 
    todo_list.append(todo)
    return todo

#endpoint to read the todo by todo id
@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id:int):
    for todo in todo_list:
        if todo.id == todo_id:
            return todo 
        return{"error":"item not found"}


#endpoint to update a todo by todo id
@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id:int, updated_todo: Todo):#indication that fucntion expects an integer as todo id
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list[index] = updated_todo
            return updated_todo
        return{"error":"Item not found"}

 #endpoint to update a todo by todo id
@app.delete("/todos/{todo_id}")
def update_todo(todo_id:int):
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            del todo_list[index]
            return {"message": "item has been deleted"}
        return{"error":"todo not found"}