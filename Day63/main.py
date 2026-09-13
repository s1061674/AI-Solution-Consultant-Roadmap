import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/todos/1",
    timeout=10
)

print(response.status_code)

data = response.json()

print(data["title"])
print(data["completed"])