import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "AI Solution Consultant",
    "body": "Learning HTTP POST",
    "userId": 7
}

try:
    response = requests.post(
        url,
        json=data,
        timeout=10
    )

    response.raise_for_status()
    result = response.json()

    
    print("建立成功")
    print(result["title"])
    print(result["userId"])
    print(result["id"])
    

except requests.RequestException as error:
    print("建立失敗")
    print(error)
