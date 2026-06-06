#1.FASTAPI ROUTES
# from fastapi import FastAPI
# app=FastAPI()
# @app.get("/")
# def home():
#     return{"message":"hello world"}
# @app.get("/users")
# def get_users():
#     return {"users":["alice","bob"]}

#2.PYDANTIC MODELS
# from fastapi import FastAPI
# from pydantic import BaseModel
# app=FastAPI()
# class user(BaseModel):
#     name:str
#     age:int
# @app.post("/users")
# def create_user(users: user):
#     return users

#3.ASYNC/AWAIT
# import asyncio
# async def greet():
#     await asyncio.sleep(2)
#     print("hello")
# asyncio.run(greet())