#1.TAKE TWO NUMBERS AS INPUT AND HANDLE DIVISION BY ZERO
# try:
#     num1=int(input("take first number:"))
#     num2=int(input("take second number:"))
#     result=num1/num2
#     print(result)
# except ZeroDivisionError:
#     print("cannot divide by zero")

#2.TAKE USER INPUT AND HANDLE THE CASE WHEN THE USER ENTERS A NON-INTEGER VALUE
# try:
#     num=int(input("enter a number:"))
#     print(num)
# except ValueError:
#     print("it is not a integer")

#3.CREATE A LIST OF 5 TIMES. ASK THE USER FOR AN INDEX AND HANDLE INVALID INDEXES
# try:
#     list=['h','e','m','a','n']
#     index=int(input("entera index(0-4):"))
#     print(list[index])
# except IndexError:
#     print("not valid integer")

#4.ASK THE USER FOR FILENAME AND HANDLE THE CASE WHERE THE FILE DOES NOT EXIST
# try:
#     filename=input("enter a file name:")
#     file=open(filename,"r")
#     content=file.read()
#     print(content)
#     file.close()
# except FileNotFoundError:
#     print("enter valid file name")

#5.MULTIPLE EXCEPTIONS HANDLE BOTH VALUEERROR AND ZEROIVISIONERROR
# try:
#     num=int(input("enter a number:"))
#     result=num/0
#     print(result)
# except ValueError:
#     print("enter a valid integer")
# except ZeroDivisionError:
#     print("zero cannot be divided")

#6.TAKE AN INTEGER INPUT .IF NO EXCEPTION OCCURS,PRINT THE SQUARE OF THE NUMBER USING THE ELSE BLOCK
# try:
#     num=int(input("enter a number:"))
#     if num>0:
#        result=num**2
#        print(result)
#     else:
#        print("number is less than the zero")
# except ValueError:
#     print("enter a valid integer")

#7.OPEN A FILE INSIDE TRY AND ENSURE A MESSAGE IS PRINTED FROM FINALLY REGARDLESS OF SUCCESS OR FAILURE
# try :
#     file=open("ppractice/hello.txt","r")
#     content=file.read()
#     print(content)
# except FileNotFoundError:
#     print("file not found")
# finally:
#     print("completed")

#8.CUSTOM EXCEPTION WITH RAISE . ASK THE USER OF AGE ,RAISE A VALUERROR IF AGE IS NEGATIVE
# try:
#     age=int(input("enter your age:"))
#     if age<0:
#         raise ValueError("age cannot be negative")
#     print(age)
# except ValueError as e:
#     print("error:",e)

#9.ASK THE USER FOR A PASSWORD,RAISE AND EXCEPTION IF THE PASSWORD LENGHT IS LESS THAN 8 CHARACTERS
# try:
#     password=input("enter your password:")
#     if len(password)<8:
#         raise ValueError("password is less than 8 characters")
#     print("password accepted")
# except ValueError as e:
#     print("error",e)
    
#10.CREATE A BALANCE VARIABLE,ASK FOR WITHDRAWAL AMOUNT,RAISE AN EXCEPTION IF AMOUNT EXCEEDS BALAMCE ,HANDLE THE EXCEPTION AND DISPLAY AN APPROPRIATE MESSAGE
# try :
#     balance=5000
#     amount=float(input("enter your withdrawal amount:"))
#     if amount>balance:
#         raise ValueError("your balance is low")
#     balance-=amount
#     print("withdrawal successful")
#     print("remaining balance:",balance)
# except ValueError as e:
#     print("error:",e)