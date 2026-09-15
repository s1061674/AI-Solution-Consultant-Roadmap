import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "HCK API",
    "body": "Learning POST",
    "userId": 1
}

try:
    response = requests.post(
        url,
        json=data,
        timeout=10
    )

    response.raise_for_status()
    result = response.json()

    
    print("POST 成功")
    print(result["title"])
    print(result["id"])
    

except requests.RequestException as error:
    print("POST 失敗")
    print(error)

