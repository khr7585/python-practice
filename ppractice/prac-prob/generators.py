#1.CREATE A GENERATOR THAT YIELDS NUMBERS FROM 1 TO 10
# gen=(x for x in range(1,11))
# print(gen)
# for value in gen:
#     print(value)

#2.CREATE A GENERATOR THAT YIELDS EVEN NUMBERS BETWEEN 1 AND 50
# even=(x for x in range(1,51) if x%2==0)
# print(even)
# for value in even:
#     print(value)

#3.CREATE A GENERATOR THAT YIELDS SQUARES OF NUMBERS FROM 1 TO 20
# sq=(x**2 for x in range(1,21))
# print(sq)
# for value in sq:
#     print(value)

#4.CREATE A GENERATOR THAT YIELDS CHARACTER OF A TSRING ONE BY ONE
# string="hemanth"
# char=(x for x in string)
# print(char)
# for value in char:
#     print(value)

#5.CREATE A GENERATOR THAT YIELDS ELEMENTS OF A LIST IN REVERSE ORDER
# def rev(list):
#     for item in reversed(list):
#         yield item
# num=[1,2,3,4,5]
# for nums in rev(num):
#     print(nums)

#6.CREATE AN INFINITE GENERATOR THAT YIELDS NATRURAL NUMBERS STARTING FROM 1
# def n():
#     num=1
#     while True:
#         yield num 
#         num+=1
# gen=n()
# for _ in range(10):
#     print(next(gen))

#7.CREATE A FIBONACCI GENERATOR THAT YIELDS THE FIRST N FIBONOCCI NUMBERS
# def fib(n):
#     a,b=0,1
#     for _ in range(n):
#         yield a
#         a,b =b,a +b
# for num in fib(10):
#     print(num)

#8.CREATE A GENERATOR THAT YIELDS ONLY VOWELS FROM A GIVEN STRING
# string="hemAntH"
# gen=(x for x in string if x in "aeiouAEIOU")
# print(gen)
# for value in gen:
#     print(value)

#9.CREATE A GENERATOR THAT YIELDS PRIME NUMBERS UPTO N.
# def prime(n):
#     for num in range(2,n+1):
#         is_prime=True
#     for i in range(2,int(num**0.5)+1):
#         if num%i==0:
#             is_prime=False
#             break
#     if is_prime:
#         yield num
# for pri in prime(20):
#     print(pri)

#10.CREATE A GENERATOR THAT READS A LIST AND YIELDS ONLY NUUMBERS GREATER THAN 50
# arr=[5,56,6,983,22,12,65]
# gen=(x for x in arr if x>50)
# print(gen)
# for value in gen:
#     print(value)