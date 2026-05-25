# 1.LIST COMPREHENSIONS
# numbers=[1,2,3,4,5]
# squares=[x*x for x in numbers]
# print(squares)

# numbers=[1,2,6,9,1,5,7,9]
# odd=[x for x in numbers if x%2!=0]
# print(odd)

# 2.DICTIONARY COMPREHENSION
# numbers=[1,2,3,4]
# square_dict={x:x*x for x in numbers}
# print(square_dict)

# 3.SET COMPREHENSION
# numbers=[1,2,3,5,2,1,3,4,4]
# unique_squares={x*x for x in numbers}
# print(unique_squares)

# 4.GENERATOR COMPREHENSION
# numbers=[1,2,3,4]
# gen=(x*x for x in numbers)
# print(gen)
# for value in gen:
#     print(value)