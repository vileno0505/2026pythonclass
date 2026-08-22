#什麼是 RSS？
#RSS（全稱：RDF Site Summary；Really Simple Syndication），是一種訊息來源格式規範。
# 簡單來說 RSS 能夠讓使用者訂閱網站，當訂閱的網站有新文章時能夠獲得通知。


import requests
import bs4
url = 'https://feeds.feedburner.com/rsscna/intworld'
response = requests.get(url)

#rss的features不要用html.parser，改成用xml或lsml
soup = bs4.BeautifulSoup(response.text, 'xml')


items = soup.find_all('item')  #抓出單篇文章區塊
for item in items:
    title = item.find('title').text   #抓標題文字
    content = item.find('description').text   #抓文章內容
    print(title)
    print(content)