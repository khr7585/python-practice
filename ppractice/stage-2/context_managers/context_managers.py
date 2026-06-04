# with open("ppractice/hello.txt", "r") as file:
#     content = file.read()
# print(content)

# class mycontext:
#     def __enter__(self):
#         print("entering")
#         return self
#     def __exit__(self, exc_type, exc, tb):
#         print("exiting")
# with mycontext():
#     print("inside block")

# from contextlib import contextmanager
# @contextmanager
# def my():
#     print("start")
#     yield
#     print("end")
# with my():
#     print("inside")
