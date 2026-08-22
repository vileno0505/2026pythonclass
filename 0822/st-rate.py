import streamlit as st
import requests
import bs4


st.title('取得匯率')

currency = st.selectbox(
    '請選擇貨幣',
    ['USD','JPY','CNY','EUR']
)

if st.button('取得'):
    url = 'https://www.esunbank.com/zh-tw/personal/deposit/rate/forex/foreign-exchange-rates'
    response = requests.get(url)
    htmlfile = bs4.BeautifulSoup(response.text, 'html.parser')
    title = htmlfile.select_one(f'.{currency} .title-item:nth-of-type(2)').text.strip()
    rate = htmlfile.select_one(f'.{currency} .CashSBoardRate').text

    #st.write(rate)

    st.success(f'{title}匯率為{rate}')
    st.info(f'{title}匯率為{rate}')
    st.warning(f'{title}匯率為{rate}')