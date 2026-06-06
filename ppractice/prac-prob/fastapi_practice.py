#1.CREATE A FASTAPI APPLICATION WITH A ROUTE / THAT RETURNS:{"MESSAGE":"WELCOME TO FASTAPI"}
# from fastapi import FastAPI
# app=FastAPI()
# @app.get("/")
# def home():
#     return {"message":"welcome to fastapi"}

#2.CREATE A ROUTE:/USERS/{USER_ID} THAT RETURNS THE GIVEN USER I
# from fastapi import FastAPI
# app=FastAPI()
# @app.get("/users/{user_id}")
# def get_user(user_id:int):
#     return {"user_id":user_id}

#3.CREATE A ROUTE:/search?name=Hemanth THAT RETURNS {"name": "Hemanth"}
# from fastapi import FastAPI
# app=FastAPI()
# @app.get("/search")
# def search(name:str):
#     return {"name":name}

#4.CREATE A STUDENT MODEL WITH:NAME(STR),AGE(INT),COURSE(STR) ACCEPT STUDENT DATA THROUGH A POST REQUEST
# from fastapi import FastAPI
# from pydantic import BaseModel
# app=FastAPI()
# class user(BaseModel):
#     name:str
#     age:int
#     course:str
# @app.post("/students")
# def c_stu(student:user):
#     return {
#         "message":"student added successfully",
#         "student":student
#     }

#5.VALIDATE DATA->CREATE A PYDANTIC MODEL PRODUCT WITH : NAME(STR) ,PRICE(FLOAT),QUANTITY(INT) RETURN THE SUBMITTED PRODUCT DETAILS
# from fastapi import FastAPI
# from pydantic import BaseModel
# app=FastAPI()
# class products(BaseModel):
#     name:str
#     price:float
#     quantity:int
# @app.post("/product")
# def pro(pro:products):
#     return {
#         "message":"submmitted",
#         "product":pro
#     }

#6.CREATE A ROUTES:GET/BOOKS,POST/BOOKS,DELETE/BOOKS/{ID} EACH ROUTE SHOULD RETURN A SIMPLE MESSAGE
# from fastapi import FastAPI
# app=FastAPI()
# @app.get("/books")
# def get_books():
#     return {"message":"list of books"}
# @app.post("/books")
# def add_books():
#     return {"message":"book added successfully"}
# @app.delete("/books/{id}")
# def delete_book(id:int):
#     return {"message":f"book with id {id} deleted successfully"}
    
#7.CREATE AN ASYNC ROUTE:@app.get("/wait") THAT WAITS FOR 3 SECONDS USING:await asyncio.sleep(3) AND THEN RETURNS:{"STATUS":"COMPLETED"}
# from fastapi import FastAPI
# import asyncio
# app=FastAPI()
# @app.get("/wait")
# async def wait_route():
#     await asyncio.sleep(3)
#     return {"status":"completed"}

#8.CREATE AN ASYNC FUNCTION:async def fetch_data(): THAT WAITS FOR 2 SECONDS AND RETURNS:"Data received" CALL IT FROM AN ASYNC ROUTE
# import asyncio
# from fastapi import FastAPI
# app=FastAPI()
# async def fetch_data():
#     await asyncio.sleep(2)
#     return "data received"
# @app.get("/data")
# async def get_data():
#     result=await fetch_data()
#     return {"message":result} 

#9.CREATE A PYDANTIC MODEL:   class User(BaseModel):username: str,email: str,password: str CRFATE A POST ROUTE /REGISTER THAT ACCEPTS USER DETAILS AND RETURNS A SUCCESS MESSAGE
# from pydantic import BaseModel
# from fastapi import FastAPI
# app=FastAPI()
# class User(BaseModel):
#     username: str
#     email: str
#     password: str
# @app.post("/register")
# def register_user(user:User):
#     return{
#         "message":"user registered successfully",
#         "username":user.username,
#         "email":user.email
#     }

#10.CREATE AN EMPLOYEE MODEL:ID(INT),NAME(STR),DEPT(STR) CREATE:POST/EMPLOYEE,GET/EMPLOYEE STORE EMPLOYEES IN A PYTHON LIST AND RETRIVE THEM BY ID
# from fastapi import FastAPI
# from pydantic import BaseModel
# app = FastAPI()
# class Employee(BaseModel):
#     id: int
#     name: str
#     department: str
# employees = []
# @app.post("/employee")
# def add_employee(employee: Employee):
#     employees.append(employee)
#     return {"message": "Employee added successfully"}
# @app.get("/employee/{id}")
# def get_employee(id: int):
#     for employee in employees:
#         if employee.id == id:
#             return employee
#     return {"message": "Employee not found"}