## what is SQLModel?
Ans: SQLModel is a Python library designed to streamline database interactions by leveraging Python's type annotations. It simplifies the creation and manipulation of database schemas through a declarative syntax, making it both intuitive and efficient. Key features include automatic SQL query generation from defined models, robust CRUD operations support, type-safe data validation, and seamless integration with popular async frameworks like FastAPI and databases like SQLAlchemy. SQLModel enhances developer productivity by reducing boilerplate code and ensuring data integrity, making it a powerful tool for modern Python applications.

### Main key features about SQLModel 
* SQLModel, created by the author of FastAPI, simplifies interactions with SQL databases in FastAPI applications.
* It combines the power of SQLAlchemy and Pydantic, reducing code duplication and optimizing the developer experience.
* Serving as a lightweight layer over Pydantic and SQLAlchemy, SQLModel is meticulously designed for seamless compatibility with both.

## To Learn More About SQLModel 
(https://sqlmodel.tiangolo.com/)


## 

# FastAPI CRUD Application
* This repository contains a simple CRUD (Create, Read, Update, Delete) application built with FastAPI, SQLAlchemy, and PostgreSQL. It demonstrates basic RESTful API operations for managing Todo items.

# Files Explanation

## main.py
* This file serves as the main entry point for the FastAPI application. It defines various CRUD operations using FastAPI endpoints.
```
POST /todos/: Create a new Todo item.
GET /todos/: Retrieve a list of Todo items with optional pagination.
GET /todos/{todo_id}: Retrieve a single Todo item by its ID.
PUT /todos/{todo_id}: Update a Todo item.
DELETE /todos/{todo_id}: Delete a Todo item.
```
## crud.py
```
Contains CRUD operations that interact directly with the database using SQLAlchemy ORM.
create_todo: Create a new Todo item in the database.
get_todos: Retrieve multiple Todo items with pagination.
get_todo: Retrieve a single Todo item by its ID.
update_todo: Update a Todo item in the database.
delete_todo: Delete a Todo item from the database.
```

## models.py
* Defines the SQLAlchemy Todo model representing the structure of Todo items stored in the database.

## Databases.py

### Todo: 
* SQLAlchemy model with fields id, title, description, and completed.
database.py
* Configures the database connection using SQLAlchemy.

### engine: 
Creates a PostgreSQL database engine using SQLAlchemy.
SessionLocal: Provides a session factory to create database sessions for CRUD operations.
schemas.py
Defines Pydantic models used for data validation and serialization.

### TodoBase: 
Base schema for Todo items with title and optional description.

### TodoCreate: 
Schema for creating Todo items.

### TodoUpdate: 
Schema for updating Todo items, including completed status.

### Todo: 
Schema representing Todo items with id, title, description, and completed.

## To run the FastAPI application
 open the terminal and navigate into the project directory and run this command 
 ```
 poetry run uvicorn main:app --reload 
 ```
* Poetry keyword asks the poetry to run the peoject
* uvicorn is the package that runs the project 
* "main" keyword indicates the name of the file "main.py", ps it's not oligatory, you can name it anything 
* "app" keyword indicates the object name created in the "main.py" file 
* "-- reload" keyword reloads the server everytime there's been a slightiest change otherwise you have to reload it manually by typing the run command which is quite frustrating so the "--reload" flag works best for me 