import streamlit as st
import requests
import bs4

st.title('RSS')

rss_web = {'證交所':'https://www.twse.com.tw/rwd/zh/news/feed?type=rss',
             '衛福部':'https://www.mohw.gov.tw/rss-16-1.html',
             '中央社國際新聞':'https://feeds.feedburner.com/rsscna/intworld',
           '自由時報即時新聞':'https://news.ltn.com.tw/rss/all.xml',
           'BBC News | News Front Page | UK Edition':'http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/front_page/rss.xml',
           'NHK主要ニュース':'https://news.web.nhk/n-data/conf/na/rss/cat0.xml',
           'NHKニュース 文化・エンタメ':'https://news.web.nhk/n-data/conf/na/rss/cat2.xml',
           }

result = st.selectbox('請選擇要檢視的RSS', rss_web.keys()) #選項中的option顯示字典中的keys
count = st.selectbox('請選擇筆數',[5,10,15,20])

if st.button('取得'):
    response = requests.get(rss_web[result], verify=False)
    soup = bs4.BeautifulSoup(response.text, 'xml')
    items = soup.find_all('item')
    #rss = []
    for item in items[:int(count)]:
        title = item.find('title').text
        # title = item.title.text
        #rss.append({'title': title, 'pubDate': item.pubDate.text})

        #st.write(title)

        st.markdown(f'- {title}--{item.pubDate.text} {item.link.text}')