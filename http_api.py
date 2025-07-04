import requests


url = "https://jsonplaceholder.typicode.com/posts"

# response = requests.get(url)

# print(response.json())
# print(response.status_code)

data = {
    "userId" : 1,
    "title" : "Hi",
    "body": "Hello Python"
}

responsepost = requests.post(url,json=data)
print(responsepost.json())
print(responsepost.status_code)
response = requests.get(url)
# print(response.json())
