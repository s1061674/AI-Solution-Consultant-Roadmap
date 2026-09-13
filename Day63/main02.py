import requests

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/todos/999999",
        timeout=10
    )

    response.raise_for_status()

    data = response.json()
    print(data)

except requests.exceptions.RequestException as error:
    print("API 請求失敗")
    print(error)