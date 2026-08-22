#在輸出的excel資料前加入編號
#Python 的 enumerate() 函數可以在迴圈中遍歷可迭代物件（如串列、字串）時，同時獲取元素的「索引」和「值」，免去手動管理計數變數的麻煩。

import requests
import bs4
import openpyxl

workbook=openpyxl.Workbook()
sheet=workbook.active

url='https://www.taoyuancollege.com.tw/all-courses?category=employed'
response=requests.get(url)
htmlfile=bs4.BeautifulSoup(response.text,'html.parser')

courses = htmlfile.find_all('div',class_='course-item')

for i,course in enumerate(courses):
    #例外處理
    try:
        title=course.find('h5',class_='card-title').text
        # duration = course.find('small',class_='text-muted').text #抓到的資料不是我們想要的
        duration=course.select_one('.info-row:nth-of-type(2) small').text
        end=course.find('small',class_='text-success').text
    except:
        continue
    print(title)
    print(duration)
    print(end.strip()) #strip去除空格
    print('-'*100)

    sheet.append([i+1,title,duration,end.strip()])

workbook.save('test2.xlsx')