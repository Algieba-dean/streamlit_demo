import streamlit as st
import time

if "data" not in st.session_state:
    st.session_state.data = list()

app = st.text_input("在这里留下你的app链接吧:")
submit_button = st.button("加入其中")

if submit_button and app:
    latest_iteration = st.empty()

    bar = st.progress(0)
    st.write(f"{app} 正在加入豪华午餐！哈哈哈")
    for i in range(100):
        latest_iteration.text(f"完成了{i + 1}%了")
        bar.progress(i + 1)
        time.sleep(0.01)
    st.session_state.data.append(app)
    st.write(f"{app} 现已加入豪华午餐！Nice!")

for data in st.session_state.data:
    st.write("-"*len(data))
    st.write(data)