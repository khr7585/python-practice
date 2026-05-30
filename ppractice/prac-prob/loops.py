#1.PRINT NUMBERS FROM 1 TO 10
# for i in range(1,11):
#     print(i)

#2.PRINT NUMBERS FROM 10 TO 1
# for i in range(10,0,-1):
#     print(i)

#3.PRINT THE MULTIPLICATION TABLE OF A GIVEN NUMBER
# num=int(input("enter a number:"))
# for i in range(1,11):
#     print(num,"x",i,"=",num*i)

#4.FIND THE SUM OF FIRST N NATURAL NUMBERS
# n=int(input("enter a n of numbers:"))
# total=0
# for i in range(1,n+1):
#     total+=i
# print(total)

#5.FIND THE FACTORIAL OF A NUMBER
# n=int(input("enter a number:"))
# total=1
# for i in range(1,n+1):
#     total*=i
# print(total)

#6.PRINT ALL EVEN NUMBERS FROM 1 TO 100
# for i in range(0,101):
#     if i%2==0:
#         print(i)

#7.PRINT ALL ODD NUMBERS FROM 1 TO 100
# for i in range(0,101):
#     if i%2!=0:
#         print(i)

#8.GENERATE FIBONACCI SERIES UP TO N TERMS
# n=int(input("enter a number of terms:"))
# a=0
# b=1
# for i in range(n):
#     print(a,end="")
#     a,b=b,a+b

#9.COUNT THE DIGITS IN A NUMBER
# n=int(input("enter a number:"))
# count=0
# while n>0:
#     count+=1
#     n//=10
# print(count)

#10.REVERSE A NUMBER USING A LOOP
# n=int(input("enter a number:"))
# reverse=0
# while n>0:
#     digit=n%10
#     reverse=reverse*10+digit
#     n//=10
# print(reverse)
    