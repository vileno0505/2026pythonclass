#爬蟲 玉山銀行匯率 1.直接個別列出想看的匯率

import requests
import bs4
url = 'https://www.esunbank.com/zh-tw/personal/deposit/rate/forex/foreign-exchange-rates'
response = requests.get(url)
htmlfile = bs4.BeautifulSoup(response.text,'html.parser')

# print(htmlfile)

usd = htmlfile.select_one('.USD .CashSBoardRate').text
jpy = htmlfile.select_one('.JPY .CashSBoardRate').text
cny = htmlfile.select_one('.CNY .CashSBoardRate').text

print(f'美金現金銀行賣出匯率為{usd}')
print(f'日幣現金銀行賣出匯率為{jpy}')
print(f'人民幣現金銀行賣出匯率為{cny}')

