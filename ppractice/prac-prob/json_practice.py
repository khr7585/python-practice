#1.CONVERT A PYTHON DICTIONARY INTO A JSON STRING
# import json
# data={
#     "name":"hemanth",
#     "age":21
# }
# json_data=json.dumps(data)
# print(json_data)
# print(type(json_data))

#2.CONVERT A JSON STRING INTO A PYTHON DICTIONARY
# import json
# json_data='{"name":"hemanth","age":21}'
# data=json.loads(json_data)
# print(data)
# print(type(data))

#3.WRITE A DCITIONARY TO A JSON FILE
# import json
# data={"name":"hemanth","age":21}
# with open("ppractice/hello.txt","w") as file:
#     file.write(json.dumps(data))

#4.READ DATA FROM A JSON FILE
# import json
# with open("ppractice/hello.txt","r") as file:
#     data=json.load(file)
# print(data)

#5.STORE A LIST OF STUDENT RECORDS IN JSON FORMAT
# import json
# list=[
#     {"name":"hemanth","age":21,"course":"python"},
#     {"name":"jake","age":22,"course":"typescript"}]
# with open("ppractice/hello.txt","w") as file:
#     json.dump(list,file,indent=4)
# print("completed")

#6.PRETTY-PRINT JSON USING INDENTATION
# import json
# data={
#     "name":"hemanth",
#     "age":21
# }
# json_data=json.dumps(data,indent=4)
# print(json_data)

#7.EXTRACT A VALUE FROM NESTED JSON DATA
# import json
# data='''{
#     "student":{
#         "name":"hemanth",
#         "age":21,
#         "address":{
#             "city":"madanapalle",
#             "state":"ap"
#         }
#     }
# }'''
# data=json.loads(data)
# city=data["student"]["address"]["city"]
# print(city)

#8.ADD A NEW KEY-VALUE PAIR TO JSON DATA
# import json
# json_data='{"name":"hemanth","age":21}'
# data=json.loads(json_data)
# data["city"]="madanapalle"
# updated_json=json.dumps(data,indent=4)
# print(updated_json)

#9.CONVERT A PYTHON LIST INTO JSON
# import json
# list=[{"name":"hemanth","age":21}]
# data=json.dumps(list)
# print(data)
# print(type(data))

#10.READ A JSON FILE AND COUNT THE NUMBER OF RECORDS
# import json
# with open("ppractice/hello.txt","r") as file:
#     data=json.load(file)
# count=len(data)
# print(count)