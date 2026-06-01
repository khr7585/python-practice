#1.CREATE A DECORATOR THAT PRINTS "FUCNTION STARTED" BEFOR EXECUTION
# def decorator(func):
#     def wrapper():
#         print("function started")
#         func()
#     return wrapper
# @decorator
# def greet():
#     print("hello ")
# greet()

#2.CREATE A DECORATOR THAT PRINTS "FCUNTION ENDED AFTER EXECUTION"
# def decorator(func):
#     def wrapper():
#         func()
#         print("function ended")
#     return wrapper
# @decorator
# def greet():
#     print("hello ")
# greet()

#3.CREATE A DECORATOR THAT WELCOMES THE USER BEFORE A FUNCTION RUNS
# def decorator(func):
#     def wrapper():
#         print("welcome to the user")
#         func()
#     return wrapper
# @decorator
# def greet():
#     print("before")
# greet()

#4.CREATE A DECORATOR THAT LOGS THE FUNCTION NAME BEING CALLED
# def decorator(func):
#     def wrapper():
#         print("function name:",func.__name__)
#         func()
#     return wrapper
# @decorator
# def greet():
#     print("hello")
# greet()

#5.DECORATOR THAT COUNTS HOW MANY TIMES A FUNCTION IS CALLED
# count=0
# def decorator(func):
#     def wrapper():
#         global count
#         count +=1
#         print("called",count,"times")
#         func()
#     return wrapper
# @decorator
# def greet():
#     print("hello")
# greet()
# greet()
# greet()

#6.DECORATOR THAT MEASURE EXECUTION TIME OF A FUNCTION
# import time
# def decorator(func):
#     def wrapper():
#         start=time.time()
#         func()
#         end=time.time()
#         print("execution time:",end-start,"seconds")
#     return wrapper
# @decorator
# def task():
#     time.sleep(2)
#     print("task completed")
# task()

#7.DECORATOR THAT CONVERTS A FUNCTIONS OUTPUT TO UPPERCASE
# def decorator(func):
#     def wrapper():
#         return func().upper()
#     return wrapper
# @decorator
# def greet():
#     return "hello world"
# print(greet())

#8.DECORATOR THAT CHECKS WHETHER A USER IS LOGGED IN
# login=False
# def decorator(func):
#     def wrapper():
#         if login:
#             func()
#         else:
#             print("please login first")
#     return wrapper
# @decorator
# def profile():
#     print("welcome to your profile")
# profile()

#9.DECORATOR THAT REPEATS A FUNCTION 3 TIMES
# def decorator(func):
#     def wrapper():
#         for i in range(3):
#             func()
#     return wrapper
# @decorator
# def greet():
#     print("hello")
# greet()

#10.DECORATOR THAT VALIDATES POSITIVE NUMBER INPUTS
# def decorator(func):
#     def wrapper(num):
#         if num>0:
#             func(num)
#         else:
#             print("enter a positive number")
#     return wrapper
# @decorator
# def sq(num):
#     print("sq=",num*num)
# sq(5)
# sq(-2)