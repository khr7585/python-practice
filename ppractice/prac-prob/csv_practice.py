#1.CREATE A CSV FILE WITH 5 STUDENT RECORDS
# import csv
# with open("students.csv","w") as file:
#     writer=csv.writer(file)
#     writer.writerow(["name","age","marks"])
#     writer.writerow(["hemanth",21,95])
#     writer.writerow(["jake",22,90])
#     writer.writerow(["billa",22,85])
#     writer.writerow(["priya",20,80])
#     writer.writerow(["gun",23,75])
# print("created")

#2.READ AND PRINT ALL ROWS FROM A CSV FILE
# import csv
# with open("students.csv","r") as file:
#     reader=csv.reader(file)
#     for row in reader:
#         print(row)

#3.COUNT THE NUMBER OF ROWS IN A CSV FILE
# import csv
# count=0
# with open("students.csv","r") as file:
#     reader=csv.reader(file)
#     next(reader)
#     count=0
#     for row in reader:
#         count+=1
# print(count)

#4.FIND THE STUDENT WITH THE HIGHEST MARKS FROM A CSV FILE
# import csv
# highest=0
# top=""
# with open("students.csv","r") as file:
#     reader=csv.DictReader(file)
#     for row in reader:
#         mark=int(row["marks"])
#         if mark>highest:
#             highest=mark
#             top=row["name"]
# print(top)
# print(highest)

#5.ADD A NEW RECORD TO AN EXISTING CSV FILE
# import csv
# with open("students.csv","a",newline="") as file:
#     writer=csv.writer(file)
#     writer.writerow(["hello",50,35])
# print("added")

#6.CONVERT CSV DATA INTO A LIST OF DICTIONARIES
# import csv
# student=[]
# with open("students.csv","r") as file:
#     reader=csv.DictReader(file)
#     for row in reader:
#         student.append(row)
# print(student)

#7.SEARCH FOR A STUDENT BY NAME IN A CSV FILE
# import csv
# search=input("enter a search name:")
# with open("students.csv","r") as file:
#     reader=csv.DictReader(file)
#     found=False
#     for row in reader:
#         if row["name"].lower()==search.lower():
#             print("found")
#             print("name:",row["name"])
#             print("age:",["age"])
#             print("marks:",["marks"])
#             found=True
#             break
#         if not found:
#             print("not found")

#8.CALCULATE THE AVERAGE MARKS OF ALL STUDNETS
# import csv
# total=0
# count=0
# with open("students.csv","r") as file:
#     reader=csv.DictReader(file)
#     for row in reader:
#         total+=int(row["marks"])
#         count+=1
# avg=total/count
# print(avg)

#9.COPY DATA FROM ONE CSV FILE TO ANOTHER
# import csv
# with open("students.csv","r") as file:
#     readers=csv.reader(file)
#     with open("hello.csv","w",newline="") as file:
#         writer=csv.writer(file)
#         for row in readers:
#             writer.writerow(row)
# print("success")

#10.CREATE A CSV FILE CONTAINING EMPLOYEE DETAILS USING DICTWRITER
# import csv
# with open("hello.csv","w",newline="") as file:
#     field=["id","name"]
#     writer=csv.DictWriter(file,fieldnames=field)
#     writer.writeheader()
#     writer.writerow({"name":"hello","id":000})
#     writer.writerow({"name":"hemanth","id":570})
# print("success")