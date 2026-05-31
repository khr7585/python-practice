#1.CREATE A STUDENT CLASS WITH NAME AND AGE ATTRIBUTES
# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def hello(self):
#         print(f"name:{self.name}&age:{self.age}")
# s=student("hemanth",21)
# s.hello()

#2.CREATE A CAR CLASS AND DISPLAY CAR DETAILS
# class car:
#     def __init__(self,brand,price):
#         self.brand=brand
#         self.price=price
#     def print(self):
#         print(f"car brand is {self.brand} & price is {self.price}")
# c=car("suziki",2000000)
# c.print()

#3.CREATE A RECTANGLE CLASS AND CALCULATE AREA
# class rectangle:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#     def area(self):
#         return self.length*self.breadth
# r=rectangle(4,5)
# r.area()
# print(f"area of rectangle is {r.area()}")

#4.CREATE A CIRCLE CLASS AND CALCULATE CIRCUMFERENCE
# import math
# class circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def cir(self):
#         return 2*math.pi*self.radius
# c=circle(4)
# c.cir()
# print(f"cricumference of a circle is {c.cir()}")

#5.CREATE A BANKACCOUNT CLASS WITH DEPOSIT AND WITHDRAW METHODS
# class bank:
#     def __init__(self):
#         self.balance=0
#     def deposit(self,amount):
#         self.balance+=amount
#         print(f"amount={amount}")
#     def show_balance(self):
#         print(f"balacne={self.balance}")
# b=bank()
# b.deposit(200)
# b.deposit(300)
# b.show_balance()

#6.CREATE A EMPLOYEE CLASS AND DISPLAY EMPLOYEE INFORMATION
# class employee:
#     def __init__(self,name,id,salary):
#         self.name=name
#         self.id=id
#         self.salary=salary
#     def inf(self):
#         print(f"name={self.name} , id={self.id} , salary={self.salary}")
# e=employee("hemanth","23f61a0570",55000)
# e.inf()

#7.CREATE A BOOK CLASS WITH TITLE AND AUTHOR ATTRIBUTES
# class book:
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
#     def display(self):
#         print(f"title={self.title} & author={self.author}")
# b=book("halwa","khr")
# b.display()

#8.CREATE A CALCULATOR CLASS WITH ADD ,SUBTRACT,MULTIPLY,AND DIVIDE METHODS
# class calculator:
#     def add(self,a,b):
#         return a+b,a-b,a*b,a/b
# c=calculator()
# print("all=",c.add(10,5))

#9.CREATE A PERSON CLASS AND ADD A METHOD TO INTRODUCE THE PERSON
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def hello(self):
#         print(f"name:{self.name}&age:{self.age}")
# p=person("hemanth",21)
# p.hello()

#10.CREATE A LAPTOP CLASS AND PRINT ITS SPECIFICATIONS
# class laptop:
#     def __init__(self,brand,model,ram,storage):
#         self.brand=brand
#         self.model=model
#         self.ram=ram
#         self.storage=storage
#     def display(self):
#         print(f"brand={self.brand} & model={self.model} & ram={self.ram} & storage={self.storage}")
# lap=laptop("ACER","intel core i5","16gb","500gb")
# lap.display()