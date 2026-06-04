#1.create a file named message.txt and write the text:hello ,python! and welcome to file handling
# file=open("ppractice/hello.txt","w")
# file.write("hello,python!")
# file.close()

#2.READ AND DISPLAY THE CONTENTS OF MESSAGE.TXT
# file=open("ppractice/hello.txt","r")
# content=file.read()
# print(content)

#3.WRITE A PROGRAM THAT COUNTS THE NUMBER OF LINES IN A FILE NAMED DATA.TXT
# with open("ppractice/hello.txt","r") as file:
#     line_count=0
#     for line in file:
#         line_count+=1
# print(line_count)

#4.READ A FILE AND COUNT THE TOTAL NUMBER OF WORDS PRESENT IN IT
# with open("ppractice/hello.txt","r") as file:
#     content=file.read()
# words=content.split()
# print(len(words))

#5.CREATE A PROGRAM THAT ASKS THE USER FOR A NAME AND APPENDS IT TO STUDENTS.TXT WITHOUT OVERWRITING EXISTING DATA
# with open("ppractice/hello.txt","a") as file:
#     name=input("enter a name:")
#     file.write(name)

#6.READ A TEXT FILE AND PRINT THE LONGEST WORD FOUND IN THE FILE
# with open("ppractice/hello.txt","r") as file:
#     content=file.read()
# words=content.split()
# longest=max(words,key=len)
# print(longest)
        
#7.COPY THE CONTENTS OF SOURCE.TXT INTO DESTINATION.TXT
# with open("ppractice/hello.txt","r") as file:
#     content=file.read()
# with open("ppractice/sample.txt","w") as destin:
#     destin.write(content)
# print("completed")

#8.READ A FILE AND COUNT HOW MANY VOWELS (A,E,I,O,U) ARE PRESENT
# with open("ppractice/hello.txt","r") as file:
#     content=file.read()
# count=0
# for i in content:
#     if i in "aeiou":
#         count+=1
# print(count)

#9.ASK THE USER FOR A WORD AND CHECK WHETHER IT EXISTS IN A FILE
# with open("ppractice/hello.txt","r") as file:
#     content=file.read()
#     name=input("enter a word:")
#     if name in content:
#         print("word found")
#     else:
#         print("not found")

#10.READ A FILE AND CREATE ANOTHER FILE THAT CONTAINS THE SAME CONTENT BUT WITHOUT ANY BLANK LINES
# with open("ppractice/hello.txt","r") as file,open("ppractice/sample.txt","w") as files:
#     for line in file:
#         if line.strip():
#             files.write(line)
# print("removed")