import requests
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

# 実行が一回でいい処理は上とかにまとめておく
with open("secrets.txt", "r") as f:
    api_key = f.read()
    url = f"http://webservice.recruit.co.jp/hotpepper/gourmet/v1/?key={api_key}"

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/call")
def read_root():
    return {"Call": "World"}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

# ホットペッパーから情報取得(パスパラメータ用)
@app.get("/hotpep1/{large_area}")
def read_hotpep(large_area: str):
    # 実行が一回でいい処理は上とかにまとめておく
    # with open("secrets.txt", "r") as f:
    #     api_key = f.read()
    #     url = f"http://webservice.recruit.co.jp/hotpepper/gourmet/v1/?key={api_key}"

    payload = {"large_area":large_area}
    # payload = {"large_area":"Z011"}
    r = requests.get(url, params=payload)

    return {"ans": r.text}

# ホットペッパーから情報取得(クエリパラメータ用)
@app.get("/hotpep2")
def read_hotpep(large_area: str = None):
    # 実行が一回でいい処理は上とかにまとめておく
    # with open("secrets.txt", "r") as f:
    #     api_key = f.read()
    #     url = f"http://webservice.recruit.co.jp/hotpepper/gourmet/v1/?key={api_key}"

    payload = {"large_area":large_area}
    # payload = {"large_area":"Z011"}
    r = requests.get(url, params=payload)

    return {"ans": r.text}
