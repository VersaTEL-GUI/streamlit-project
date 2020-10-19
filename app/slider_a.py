import streamlit as st

'''
    生成滑动插件
    每次改变滑动的位置时，整个程序都会从上到下运行
'''

x = st.slider('x')
st.write(x)
st.write(x, 'squared is', x * x)