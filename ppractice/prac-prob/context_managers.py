#1.CREATE A CUSTOM CONTEXT MANAGER THAT PRINTS.(ENTERING...)(EXITING...) WHEN ENTERING AND LEAVING THE BLOCK
# class my():
#     def __enter__(self):
#         print("entering...")
#     def __exit__(self, exc_type, exc, tb):
#         print("exiting...")
# with my():
#     print("inside")

#2.CREATE A CONTEXT MANAGER USING A CLASS THAT OPENS A FILE AND AUTOMATICALLY CLOSES IT
# class filemanager:
#     def __init__(self,name,mode):
#         self.name=name
#         self.mode=mode
#     def __enter__(self):
#         self.file=open(self.name,self.mode)
#         return self.file
#     def __exit__(self, exc_type, exc, tb):
#         self.file.close()
#         print("file closed")
# with filemanager("sample.txt","w") as f:
#     f.write("hello world!")

#3.CREATE A CONTEXT MANAGER USING CONTEXTLIB.CONTEXTMANAGER
# from contextlib import contextmanager
# @contextmanager
# def my():
#     print("start")
#     yield
#     print("end")
# with my():
#     print("inside")

#4.CREATE A CONTEXT MANAGER THAT MEASURE HOW LONG A BLOCK TAKES TO EXCUTE
