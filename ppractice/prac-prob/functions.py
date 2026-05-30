#1.CREATE A FUNCTION TO PRINT "HELLO WORLD"
# def fun():
#     print("hello world")
# fun()

#2.CREATE A FUNCTION TO ADD TWO NUMBERS
# def add(a,b):
#     print(a+b)
# add(2,3)

#3.CREATE A FUNCTION TO FIND THE SQUARE OF A NUMBER
# def fun(a):
#     print(a**2)
# fun(4)

#4.CREATE A FUNCTION TO CHECK WHETHER A NUMBER IS EVEN OR ODD
# def fun(a):
#     if a%2==0:
#         print("it is a even number")
#     else :
#         print("it is odd number")
# fun(56)

#5.CREATE A FUNCTION TO FIND THE LARGEST OF TWO NUMBERS
# def fun(a,b):
#     if a>b:
#         print("a is largest number")
#     else:
#         print("b is largest number")
# fun(1,2)

#6.CREATE A FUNCTON TO CALCULATE FACTORIAL
# def num(a):
#     fact=1
#     for i in range(1,a+1):
#         fact*=i
#     print(fact)
# num(5)

#7.CREATE A FUNCTION TO CHECK WHETHER A NUMBER IS PRIME
# def num(a):
#     if a<=1:
#         return False
#     for i in range(2,a):
#         if a%i==0:
#             return False
#     return True
# n=int(input("enter a number:"))
# if num(n):
#     print("prime")
# else:
#     print("not prime")

#8.CREATE A FCUNTION TO REVERSE A STRING
# def fun(text):
#     return text[::-1]
# h=input("enter a text:")
# print(fun(h))

#9.CREATE A FUNCTION TO COUNT VOWELS IN A STRING
# def fun(text):
#     count=0
#     for char in text.lower():
#         if char in "aeiou":
#             count+=1
#     return count
# n=input("enter a text:")
# print(fun(n))

#10.CREATE A FUNCTION TO CLACULATE THE AREA OF A CIRCLE
# def area(radius):
#     print(3.14*radius**2)
# area(4)