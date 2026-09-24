import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {
   "userId": 999
}

try:
    response = requests.get(
    url,
    params=params,
    timeout=10
    )
    response.raise_for_status()
    data = response.json()
    print(response.url)
    print(len(data))
    if data:
        print(data[0]["title"])
    else:
        print("查無資料")

except requests.RequestException as error:
    print("API 請求失敗")
    print(error)