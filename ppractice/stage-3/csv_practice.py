#1.READING A FILE
# import csv
# with open("students.csv","r") as file:
#     reader=csv.reader(file)
#     for row in reader:
#         print(row)

#2.WRITING TO CSV FILE
# import csv
# with open("students.csv","w") as file:
#     write=csv.writer(file)
#     write.writerow(["name","age","city"])
#     write.writerow(["hemanth",21,"madanapalle"])

#3.USING DICTREADER
# import csv
# with open("students.csv","r") as file:
#     reader=csv.DictReader(file)
#     for row in reader:
#         print(row["name"],row["age"])

#4.USING DICTWRITER
# import csv
# with open("students.csv","w") as file:
#     filenames=["name","age"]
#     writer=csv.DictWriter(file,fieldnames=filenames)
#     writer.writeheader()
#     writer.writerow({"name":"hemanth","age":21})