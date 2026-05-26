# class Count:
#     def __init__(self, max):
#         self.num = 1
#         self.max = max
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.num <= self.max:
#             value = self.num
#             self.num += 1
#             return value
#         else:
#             raise StopIteration
# c = Count(6)
# for i in c:
#     print(i)


# def count(n):
#     for i in range(1, n + 1):
#         yield i
# for x in count(5):
#     print(x)