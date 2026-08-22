import requests
# import openpyxl
# wb=openpyxl.Workbook()
# sheet=wb.active
# sheet.append(['公司名稱','工作項目','地區'])

#自製搜尋器
keyword = input('請輸入關鍵字')

url=f'https://www.104.com.tw/jobs/search/api/jobs?dist=0.25&jobsource=pt_search&keyword={keyword}&pagesize=20&remoteWork=1&ro=2&transTime=5&transType=2'

header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36'
        ,'referer':'https://www.104.com.tw/jobs/search/?dist=0.25&jobsource=pt_search&keyword=%E9%81%A0%E7%AB%AF&remoteWork=1&ro=2&transTime=5&transType=2&order=15&page=2'
        }

response = requests.get(url, headers=header, verify=False)

# print(response)


# print(response.json())
json_data = response.json()
for item in json_data['data']:
    print(item['custName'])
    print(item['jobName'])
    # print(item['description'])
    print(item['jobAddrNoDesc'])
    print('=' * 100)

#     sheet.append([item['custName'], item['jobName'], item['jobAddrNoDesc']])
#
# wb.save('104.xlsx')
# #excel存檔