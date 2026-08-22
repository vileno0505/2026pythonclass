import streamlit as st

home = st.Page('home.py', title='首頁')
rate = st.Page('st-rate.py',title='取得匯率')
weather = st.Page('st-weather.py',title='取得天氣')
rss = st.Page('st-rss.py',title='RSS')

pg = st.navigation([home, rate, weather,rss])

pg.run()