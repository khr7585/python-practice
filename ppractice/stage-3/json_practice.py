#JSON FORMATT
# {
#     "name":"hemanth",
#     "age":21,
#     "skills":["python","js","java"]
# }

#IN PYTHON
# data={
#     "name":"hemanth",
#     "age":21,
#     "skills":["python","js","java"]
# }

#CONVERTING PYTHON OBJECT TO JSON string(SUE JSON.DUMPS())
# import json
# data={
#     "name":"hemanth",
#     "age":21
# }
# json_data=json.dumps(data)
# print(json_data)
# print(type(json_data))

#CONVERTING JSON TO PYTHON OBJECT
# import json
# json_data='{"name":"khr","age":21}'
# data=json.loads(json_data)
# print(data)
# print(type(data))

#WRITING JSON TO A FILE
# import json
# data={
#     "name":"hemanth",
#     "age":21
# }
# with open("ppractice/hello.txt","w") as file:
#     json.dump(data,file)

#READING JSON FROM A FILE
# import json
# with open("ppractice/hello.txt","r") as file:
#     data=json.load(file)
# print(data)