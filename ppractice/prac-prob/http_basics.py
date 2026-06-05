#1.USE THE REQUETS LIBRARY TO SEND A GET REQUEST TO:https://jsonplaceholder.typicode.com/posts/1 PRINT THE STATUS CODE AND RESPONSE DATA
# import requests
# response=requests.get("https://jsonplaceholder.typicode.com/posts/1")
# print(response.status_code)
# print("response:")
# print(response.json())

#2.FETCH ALL POSTS FROM: https://jsonplaceholder.typicode.com/posts PRINT THE TOTAL NUMBER OF POSTS RETURNED
# import requests
# response=requests.get("https://jsonplaceholder.typicode.com/posts")
# posts=response.json()
# print(len(posts))

#3.GET REQUEST WITH QUERY PARAMETERS ->SEND A GET REQUEST TO:https://jsonplaceholder.typicode.com/comments RETRIVE COMMENTS ONLY FOR POSTID=1
# import requests
# params={
#     "postid":1
# }
# response=requests.get("https://jsonplaceholder.typicode.com/comments",
#                       params=params)
# comments=response.json()
# print(len(comments))
# for comment in comments:
#     print(comment["name"])

#4.CREATE A POST USING POST -> SEND A POST REQUEST WITH:{ "title": "Python","body": "REST API Practice","userId": 1} PRINT THE CREATES RESOURCE
# import requests
# data={
#     "title": "Python",
#     "body": "REST API Practice",
#     "userId": 1
# }
# respone=requests.post("https://jsonplaceholder.typicode.com/posts",json=data)
# print(respone.json())

#5.WRITE A PROGRAM THAT SENDS A GET REQUEST AND PRINTS: "SUCCESS " IF STATUS CODE IS 200 "FAILED" OTHERWISE
# import requests
# respone=requests.get("https://jsonplaceholder.typicode.com/posts")
# if respone.status_code==200:
#     print("success")
# else:
#     print("failed")

#6.FETCH USER DATA FROM: https://jsonplaceholder.typicode.com/users/1 PRINT ONLY:NAME,EMAIL,PHONE
# import requests
# response=requests.get("https://jsonplaceholder.typicode.com/users/1")
# user=response.json()
# print("name:",user["name"])
# print("email:",user["email"])
# print("phone:",user["phone"])

#7.USE TRY-EXPECT TO HANDLE: CONNECTION ERRORS,TIMEOUT ERROS WHILE MAKING A GET REQUEST
# import requests
# try:
#     response=requests.get("https://jsonplaceholder.typicode.com/posts/1",timeout=5)
#     print(response.status_code)
#     print(response.json())
# except requests.exceptions.ConnectionError:
#     print("Connection Error: Unable to connect to the server.")
# except requests.exceptions.TimeoutError:
#     print("Timeout Error: The request took too long.")
# except requests.exceptions.RequestException as e:
#     print("an error occured:",e)
    
#8.FETCH ALL POSTS AND PRINT ONLY THE TITLES OF THE FIRST 5 POSTS
# import requests
# response=requests.get( "https://jsonplaceholder.typicode.com/posts")
# posts=response.json()
# for post in posts[:5]:
#     print(post["title"])

#9.CREATE A MENU : GET USER,GET POST,EXIT BASED ON USER INPUT,FETCH AND DISPLAY THE REQUESTED DATA
# import requests
# while True:
#     print("\n1. Get User")
#     print("2. Get Post")
#     print("3. Exit")
#     choice = input("Enter your choice: ")
#     if choice == "1":
#         user_id = input("Enter User ID: ")
#         response = requests.get(
#             f"https://jsonplaceholder.typicode.com/users/{user_id}"
#         )
#         if response.status_code == 200:
#             user = response.json()
#             print("Name:", user["name"])
#             print("Email:", user["email"])
#         else:
#             print("User not found")
#     elif choice == "2":
#         post_id = input("Enter Post ID: ")
#         response = requests.get(
#             f"https://jsonplaceholder.typicode.com/posts/{post_id}"
#         )
#         if response.status_code == 200:
#             post = response.json()
#             print("Title:", post["title"])
#             print("Body:", post["body"])
#         else:
#             print("Post not found")
#     elif choice == "3":
#         print("Exiting...")
#         break
#     else:
#         print("Invalid choice")

#10.CREATE A PROGRAM THAT: Asks for a post ID,Sends a GET request,Displays:User ID,Title,Body,Handles invalid IDs gracefully.
# import requests
# post_id = input("Enter Post ID: ")
# try:
#     response = requests.get(
#         f"https://jsonplaceholder.typicode.com/posts/{post_id}",
#         timeout=5
#     )
#     if response.status_code == 200:
#         post = response.json()
#         print("\nPost Details")
#         print("User ID:", post["userId"])
#         print("Title:", post["title"])
#         print("Body:", post["body"])
#     else:
#         print("Post not found!")
# except requests.exceptions.RequestException as e:
#     print("Error:", e)