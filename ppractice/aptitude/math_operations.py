# 1.prime number
s=int(input("enter a number:"))
count=0
for i in range(1,s+1):
    if s%i==0:
        count+=1
if count==2:
    print("it is a prime number")
else:
    print("not prime number")
    
# 2.armstrong number
n=int(input("enter a number:"))
original=n
sum=0
while n>0:
    digit=n%10
    sum=sum+(digit*digit*digit)
    n=n//10
if sum==original:
    print("armstrong number")
else:
    print("not armstrong number")
    
# 3.perfect number
s=int(input("enter a number:"))
sum=0
for i in range(1,s):
    if s%i==0:
        sum=sum+i
if s==sum:
    print("it is a perfect number")
else:
    print("it is not a perfect number")
    
# 4.neon number
s=int(input("enter a number:"))
square=s*s
sum=0
while square>0:
    digit=square%10
    sum=sum+digit
    square=square//10
if s==sum:
    print("neon number")
else:
    print("not neon number")
    
# 5.fibonacci series
n=int(input("enter a number:"))
a=0
b=1
while a<=n:
    print(a,end=" ")
    c=a+b
    a=b
    b=c

# another method
n=8
a=0
b=1
print(a,end=" ")
print(b,end=" ")
for i in range(3,n+1):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
    
# 6.factorial
n=int(input("enter a number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)

# 7.GCD
a=12
b=18
gcd=1
if a<b:
    small=a
else:
    small:b
for i in range(1,small+1):
    if a%i==0 and b%i==0:
        gcd=i
print(gcd)

# another method
a=12
b=18
while b!=0:
    temp=b
    b=a%b
    a=temp
print(a)

# 8.lcm
a=12
b=18
if a>b:
    small=a
else:
    small=b
while True:
    if small %a==0 and small %b==0:
        break
    small=small+1
print(small)

# another method
a=12
b=18
x=a
y=b
while y!=0:
    temp=y
    y=x%y
    x=temp
gcd=x
small=(a*b)//gcd
print(small)

# 9.sum of digits
n=1234
sum=0
while n>0:
    digit=n%10
    sum=sum+digit
    n=n//10
print(sum)

# 10.strong number
n=145
original=n
sum=0
while n>0:
    digit=n%10
    fact=1
    for i in range(1,digit+1):
        fact=fact*i
    sum=sum+fact
    n=n//10
if sum==original:
    print("strong number")
else:
    print("not strong number")