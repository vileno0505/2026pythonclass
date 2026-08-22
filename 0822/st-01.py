#使用streamlit將python顯示在網頁中

import streamlit as st

st.title('HELLO WORLD')
st.header('header')
st.subheader('subheader')
st.write('write')

#=======================================#

name = st.text_input('請輸入稱呼:')

currency = st.selectbox(
    '選項',['USD','JPY','EUR'])

gender = st.selectbox(
    '性別',['男','女','秘'])

if st.button('確定'):
    st.write(name)
    st.write(gender)
    st.write(currency)  #變數不用用''框起來

