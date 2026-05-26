# 1.SIMPLE DECORATOR 
# def decorator(func):
#     def wrapper():
#         print("before")
#         func()
#         print("after")
#     return wrapper
# @decorator
# def greet():
#     print("hello")
# greet()

#2.CUSTOM DECORATOR WITH ARGUMENTS
# def smart(func):
#     def wrapper(a,b):
#         if b==0:
#             print("cannot")
#             return
#         return func(a,b)
#     return wrapper
# @smart
# def divide(a,b):
#     print(a/b)
# divide(10,2)
# divide(10,0)

#3.FUNCTOOLS IN DECORATORS
# from functools import wraps
# def decorator(func):
#     @wraps(func)
#     def wrapper():
#         print("Running function")
#         func()
#     return wrapper
# @decorator
# def greet():
#     """Greeting function"""
#     print("Hello")
# print(greet.__name__)
# print(greet.__doc__)

#4.@PROPERTY DECORATOR
#without @property
# class Student:
#     def __init__(self, marks):
#         self.set_marks(marks)
#     def set_marks(self, marks):
#         self._marks = marks
#     def get_marks(self):
#         return self._marks
# s = Student(90)
# print(s.get_marks())

#with @property
# class Student:
#     def __init__(self, marks):
#         self._marks = marks
#     @property
#     def marks(self):
#         return self._marks
#     @marks.setter
#     def marks(self, value):
#         if value < 0:
#             print("Invalid marks")
#         else:
#             self._marks = value
# s = Student(90)
# print(s.marks)
# s.marks = 95
# print(s.marks)