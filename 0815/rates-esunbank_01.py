#爬蟲 玉山銀行匯率 2.互動式設計

import requests
import bs4
url = 'https://www.esunbank.com/zh-tw/personal/deposit/rate/forex/foreign-exchange-rates'


while True:
    try:
        c = input('請輸入貨幣代號(usd,cny,jpy)或輸入123結束程式:')
        if c == '123' :
            print('下次見')
            break
        response = requests.get(url)
        htmlfile = bs4.BeautifulSoup(response.text, 'html.parser')

        # 原始碼中同一個class裡的title-item有好幾個，要去指定你要拿第幾個title-item，不然都會抓到第一個：
        # .title-item = 找 class="title-item" 的元素
        # nth-of-type(2)表示同一層的同類型 HTML 標籤中，選第 2 個
        # .strip 去除空格
        title = htmlfile.select_one(f'.{c.upper()} .title-item:nth-of-type(2)').text.strip()
        rate = htmlfile.select_one(f'.{c.upper()} .CashSBoardRate').text

        #目前沒有現金匯率的另外說明
        if rate == '':
            print(f'{title}沒有現金匯率')
        else:
            print(f'{title}匯率為{rate}')

    #用try+except排除輸入錯誤的報錯
    except AttributeError :
        print('請輸入正確代號')
        continue

