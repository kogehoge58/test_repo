import requests


# エンドポイント
url = "https://uinames.com/api/?region=japan"

# API呼び出し
response = requests.get(url)

# レスポンス返却
# print(response.json())
# print(response.text)
print(response)