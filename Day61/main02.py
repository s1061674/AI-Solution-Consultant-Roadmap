import os

api_key = os.environ.get("MY_API_KEY")

if api_key:
    print("API Key 已載入")

else:
    print("找不到 API Key入")