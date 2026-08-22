from pydoc import text
import os #建立資料夾
import re #正規表達式
import requests
import bs4
import urllib.request as req #存取網址，下載網路資源，後面as req是給他一個代號，讓程式之後看到req就知道他是urllib
url='https://www.tenlong.com.tw/zh_tw/recent'
response=requests.get(url)
htmlfile=bs4.BeautifulSoup(response.text,'html.parser')

#print(response)  #確認網頁是否可抓
#print(htmlfile)  #檢視原始碼

# imgs=htmlfile.find_all('img')

# #將商品標題與圖片連結抓出來
# for img in imgs:
#     #print('img')
#     try:
#         print(img['alt'])
#         print(img['src'])
#         print('-' * 80)
#     except:
#         continue

os.makedirs('img',exist_ok= True)
books=htmlfile.find_all('li',class_='single-book')
for i,book in enumerate(books):
    title=book.select_one('.title a').text
    title=re.sub(r'[|\/?:<>]','_',title)
    title=re.sub(r'[\x00-\x1f]','',title)
    img_url=book.find('img')['src']
    print(img_url)
    req.urlretrieve(img_url, f'img/{title}.jpg')