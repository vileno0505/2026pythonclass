#讓python一次抓出指定數量的資料

import requests
import openpyxl

#header不需要一直重複所以放在for迴圈外即可
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36'}

workbook=openpyxl.Workbook() #開啟excel
sheet=workbook.active #啟動工作表

sheet.append(['類型','說明','地址','金額'])


for i in range(0,150,30):
    print(i)

    #加入for迴圈之後要把原本firstRow的數字改成變數，變數要加{}
    #記得退一格，才能包進for迴圈裡
    url=f'https://bff-house.591.com.tw/v3/web/rent/list?regionid=6&firstRow={i}'
    #response要跟著url跑，所以雖然不需要重複但不可以送出for迴圈
    response = requests.get(url, verify=False, headers=header)

    print(response.json())
    json_data = response.json()
    for item in json_data['data']['items']:
        print(item['kind_name'])
        print(item['title'])
        print(item['address'])
        print(item['price'])
        print('=' * 100)

        sheet.append([item['kind_name'],item['title'],item['address'],item['price']])

workbook.save('test3.xlsx') #excel存檔