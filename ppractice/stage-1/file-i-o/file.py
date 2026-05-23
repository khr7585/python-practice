#1.WRITING TO A FILE
# file=open("hello.txt","w")
# file.write("hello,python!")
# file.close()

# lines=["line1/n","line2/n","line3/n"]
# file=open("hello.txt","w")
# file.writelines(lines)
# file.close()


#2.READING FROM A FILE
# file=open("hello.txt","r")
# content=file.read()
# print(content)
# file.close()

# file = open("hello.txt", "r")
# line = file.readline()
# print(line)   
# file.close()

# file = open("hello.txt", "r")
# lines = file.readlines()
# print(lines) 
# file.close()


#3.WITH STATEMENT(automatically closes the file-no need to call close())
# with open("hello.txt","w") as f:
#     f.write("hello world")
# with open ("hello.txt","r") as f:
#     content=f.read()
#     print(content)
# with open("hello.txt","a") as f:
#     f.write("\nnew line added")


#4.APPEND MODE
# with open("hello.txt","a") as f:
#     f.write("\nnew line added")