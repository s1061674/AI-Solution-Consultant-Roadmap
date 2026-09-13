import requests

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/todos/1",
        timeout=10
    )

    response.raise_for_status()

    data = response.json()
    print("API 請求成功")
    print(data["title"])
    
except requests.exceptions.RequestException as error:
    print("API 請求失敗")
    print(error)