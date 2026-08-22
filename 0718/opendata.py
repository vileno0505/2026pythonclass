#政府資料開放平台 https://data.gov.tw/

import requests

url='https://tcgbusfs.blob.core.windows.net/dotapp/news.json'

response=requests.get(url)

print(response.json())

#json_data = response.json()
for item in json_data:
    print(item['chtmessage'])
    print(item['starttime'])
    print(item['endtime'])
    print(item['updatetime'])
    print(item['content'])