import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {
   "userId": 2
}

try:
    response = requests.get(
    url,
    params=params,
    timeout=10
    )
    response.raise_for_status()
    data = response.json()
    
    if data:
        print("查詢成功")
        print(f"共有 {len(data)} 筆資料")
        print(f"第一篇：{data[0]['title']}")
    else:
        print("查無資料")

except requests.RequestException as error:
    print("API 請求失敗")
    print(error)