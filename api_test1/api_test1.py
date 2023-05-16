import requests
# apiキーは別ファイルから取得、pg内にあるとあげられない

# closeを忘れるかも知れない書き方
# f = open('secrets.txt', 'r', encoding='UTF-8')
# api_key = f.read()
# f.close()

# closeを忘れない書き方
with open("secrets.txt", "r") as f:
    api_key = f.read()

url = f"http://webservice.recruit.co.jp/hotpepper/gourmet/v1/?key={api_key}"
payload = {"large_area":"Z011"}
r = requests.get(url, params=payload)

print(r.text)

