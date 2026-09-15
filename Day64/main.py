import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "Learn API",
    "body": "Day64 POST practice",
    "userId": 1
}

response = requests.post(
    url,
    json=data,
    timeout=10
)

print(response.status_code)

result = response.json()

print(result)