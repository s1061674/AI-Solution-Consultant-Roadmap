import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 1
}

response = requests.get(
    url,
    params=params,
    timeout=10
)

response.raise_for_status()

data = response.json()

print(response.url)
print(len(data))
print(data[0]["title"])