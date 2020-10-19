import streamlit as st


st.markdown('### 三次方计算器 :sunglasses:')
x = st.slider('输入一个数字')
st.write(x, '的三次方为：', x**3)
st.markdown('> Streamlit挺好用 :+1:')