# import requests
# url=('https://www.ptt.cc/bbs/WorldCup/index.html')
# response=requests.get(url)
# print(response.text)



import requests
import bs4
url=('https://www.ptt.cc/bbs/WorldCup/index.html')
response=requests.get(url)
htmlfile=bs4.BeautifulSoup(response.text,'html.parser')

# print(htmlfile.find_all('title'))  ---尋找全部
# print(htmlfile.find('a'))  ---尋找第一個

#找到全部的<a>，會顯示很長很長一串，用for迴圈把項目都繞出來列出
# print(htmlfile.find_all('a'))
# for item in htmlfile.find_all('a'):
#     print(item)

#尋找連結標題
#寫法1
# titles=htmlfile.find_all('div',{'class':'title'})
#寫法2
titles=htmlfile.find_all('div',class_='title')

for title in titles:
    # print(title)
    if title.find('a')is None:
        continue
    print(title.find('a').text)

print('-' * 80)

rent = htmlfile.find_all('div',class_='r-ent')
for item in rent:
    if item.find('a') is None:
        continue
    print(item.find('div', class_='title').find('a').text)
    print(item.find('div', class_='author').text)
    print('-' * 50)