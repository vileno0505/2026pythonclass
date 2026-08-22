import streamlit as st

st.title('首頁')

st.title('HELLO WORLD')
st.header('大標題')
st.subheader('小標題')
st.write('內文')

with open('0822/test.md', 'r', encoding='utf-8')as f:
    st.markdown(f.read())