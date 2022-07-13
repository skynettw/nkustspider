from pymongo import MongoClient
conn = MongoClient("mongodb://root:example@localhost:27017/")
db = conn.nkust
collection = db.news

place = input("請輸入國家的名稱(英文)：")
while place!="exit":
    find_cmd = {"bornplace":{'$regex' : place}}
    rows = collection.find(find_cmd)
    for row in rows:
        print(row['author'], end=":")
        print(row['bornplace'])
    place = input("請輸入國家的名稱(英文)：")        