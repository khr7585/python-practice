#EXAMPLE
# import requests
# response = requests.get("https://api.github.com")
# print(response.status_code)

#GET METHOD
# import requests
# response=requests.get("https://jsonplaceholder.typicode.com/posts/1")
# print(response.json())

#POST METHOD
# import requests
# data={
#     "title":"python",
#     "body":"learning rest apis",
#     "userid":1
# }
# respone=requests.post("https://jsonplaceholder.typicode.com/posts/",json=data)
# print(respone.json())