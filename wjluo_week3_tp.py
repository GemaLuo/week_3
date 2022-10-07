#要求一

import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response)
spot_li=data["result"]["results"]
with open("data.csv", "w", encoding="utf-8") as file:
        for date,spot,addr,long,lati,pic in zip(spot_li,spot_li,spot_li,spot_li,spot_li,spot_li):
            if (date["xpostDate"][:4]>="2015"):#僅輸入2015年後的資料 if假設date大於等於2015為true
                file.write(spot["stitle"]+","+addr["address"][5:8]+","+long["longitude"]+","+lati["latitude"]+","+pic["file"][:pic["file"].lower().index("jpg")]+"jpg"+"\n") #照片網址使用index索引：注意大小寫


