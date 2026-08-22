import requests

#一般網址有可能出現SSLError，就不能貼原本的網址(第一層最基本的防護，http's'的s)
# url='https://rent.591.com.tw/list?region=6&page=2'

#第二層拒絕訪問的開門方法
#f12→網路→list開頭的→標頭→要求網址
url='https://bff-house.591.com.tw/v3/web/rent/list?timestamp=1784347565085&regionid=6&firstRow=0'

#標頭最底下的user-agent (讓系統認為爬蟲是人)
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36'}

response = requests.get(url, verify=False, headers=header)

#json內為純資料，可以從這裡抓資料出來
print(response.json())
json_data = response.json()
for item in json_data['data']['items']:
    print(item['kind_name'])
    print(item['title'])
    print(item['address'])
    print(f'${item['price']}')
    print('=' * 100)