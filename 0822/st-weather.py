import streamlit as st
import requests

st.title('天氣資訊')

q = st.text_input('請輸入查詢地區(例:taipei,tw)')

if st.button('查詢'):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={q}&appid=b1ecbccd638b763d489602917ba47cc3&units=metric&lang=zh_TW'
    response = requests.get(url)
    data = response.json()
    if data['cod'] != 200:
        st.error('沒有該城市或發生錯誤')
    else:
        temp = data['main']['temp']
        temp_max = data['main']['temp_max']
        temp_min = data['main']['temp_min']
        feels = data['main']['feels_like']

        desc = data['weather'][0]['description']

        with st.container(border=True):
            st.image(f'https://openweathermap.org/payload/api/media/file/{data['weather'][0]['icon']}.png')
            st.write(f'目前氣溫:{temp}°C')
            st.write(f'最高溫:{temp_max}°C')
            st.write(f'最低溫:{temp_min}°C')
            st.write(f'體感溫度:{feels}°C')
            st.write(f'狀態:{desc}')





#下拉式清單的寫法

# weather = st.selectbox(
#     '請選擇地區',
#     ['Taipei,TW','Taoyuan,TW','Tokyo,JP','Yokohama,JP'])
#
# if st.button('確定'):
#     url = f'https://api.openweathermap.org/data/2.5/weather?q={weather}&appid=b1ecbccd638b763d489602917ba47cc3&units=metric&lang=zh_TW'
#     response = requests.get(url)
#     data = response.json()
#     temp = data['main']['temp']
#     temp_max = data['main']['temp_max']
#     temp_min = data['main']['temp_min']
#     feels = data['main']['feels_like']
#
#     desc = data['weather'][0]['description']
#
#     st.success(f'{weather}：目前氣溫:{temp}°C，最高溫:{temp_max}°C，最低溫:{temp_min}°C，體感溫度:{feels}°C，{desc}')