import requests
import bs4
import openpyxl #把檔案存入excel

workbook=openpyxl.Workbook() #開啟excel
sheet=workbook.active #啟動工作表

url='https://www.taoyuancollege.com.tw/all-courses?category=employed'
response=requests.get(url)
htmlfile=bs4.BeautifulSoup(response.text,'html.parser')

courses = htmlfile.find_all('div',class_='course-item')

for course in courses:
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

    sheet.append([title,duration,end.strip()])
    #將資料存成串列，for每繞一圈存一次

workbook.save('test.xlsx') #excel存檔