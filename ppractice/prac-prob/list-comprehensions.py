#1.CREATE A LIST OF SQUARES FROM 1 TO 20 USING A LIST COMPREHENSION
# squares=[x*x for x in range(1,21)]
# print(squares)

#2.CREATE A LIST CONTAINING ONLY EVEN NUMBERS FROM 1 TO 50
# even=[x for x in range(1,50) if x%2==0]
# print(even)

#3.NUMS=[1,2,3,4,5] CREATE A NEW LIST WITH EACH NUMBER DOUBLED
# nums=[1,2,3,4,5]
# new=[x*2 for x in nums]
# print(new)

#4.WORDS=["APPLE","BANANA","CHERRY"] create a list of word lengths
# words=["apple","banana","cherry"]
# len=[len(word) for word in words]
# print(len)

#5.NAMES=["JOHN","ALICE","BOB"] CONVERT ALL NAMES TO UPPERCASE
# names=["john","alice","bob"]
# upp=[name.upper() for name in names]
# print(upp)

#6.CREATE A LIST OF NUMBERS FROM 1 TO 100 THAT ARE DIVISBLE BY BOTH 3 AND 5
# div=[i for i in range(1,100) if i%3==0 and i%5==0]
# print(div)

#7.STRINGS=["123","456","789"] CONVERT THEM INTO INTEGERS
# strings=["123","456","789"]
# int=[int(str) for str in strings]
# print(int)

#8.NUMS=[1,2,3,4,5] CREATE A LIST CONTAINING ONLY ODD NUMBERS
# nums=[1,2,3,4,5]
# odd=[i for i in nums if i%2!=0]
# print(odd)

#9.CREATE A LIST OF TUPLES : [(1,1),(2,4),(3,9),....,(10,100)]
# result=[(n,n**2)for n in range(1,11)]
# print(result)

#10.FLATTEN THE FOLLOWING NESTED LIST : [[1,2],[3,4],[5,6]]  TO [1,2,3,4,5,6]
# list=[[1,2],[3,4],[5,6]]
# li=[num for sublist in list for num in sublist]
# print(li)