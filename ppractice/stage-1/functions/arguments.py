#1.POSTIONAL ARGUMENTS(order mtters-passed by position)
# def describe(name,age,city):
#     print(f"{name} is {age} years old from {city}")
# describe("hemanth",21,"madanapalle")


#2.KEYWORD ARGUMENTS(pass by name-order doesn't matter)
# def describe(name,age,city):
#     print(f"{name} is {age} years old from {city}")
# describe("hemanth" ,age=21,city="madanapalle")


#3.DEFAULT ARGUMENTS(give a parameter a fallback value)
# def describe(name,city="madanapalle"):
#     print(f"hello {name} from {city}")
# describe("hemanth")
# describe("jake","banglore")
# describe("gun",city="chennai")


#4.*ARGS -VARIABLE POSITIONAL(accept any number of positional arguments)
# def add_all(*nums):
#     print(type(nums))
#     return sum(nums)
# print(add_all(1,2,3,4,5))

#mix with normal args
# def show(prefix,*items):
#     for item in items:
#        print(f"{prefix}:{item}")
# show("fruit","apple","banana","mango")


#5.**KWARGS-VARIBALE KEYWORD(accept any number of keyword arguments)
# def profile(**info):
#     print(type(info))
#     for key,val in info.items():
#         print(f"{key}:{val}")
# profile(name="hemanth",age=21,gpa=8.34,city="madanapalle")

#mix args and kwargs
# def everything(a,b,*args,**kwargs):
#     print("a:",a)
#     print("b:",b)
#     print("args:",args)
#     print("kwargs:",kwargs)
# everything(1,2,3,4,name="hemanth",city="madanapalle")