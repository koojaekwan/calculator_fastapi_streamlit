import streamlit as st
import json
import requests


# 사용자가 웹에서 보이는 화면
# 두 수를 사용자는 입력하고 연산자를 선택
# 결과를 dictionary로 받아 fast api로 requerts모듈을 활용해 post -> fast api로부터 결과를 받아옴
# 웹 상에서 결과를 보여줌
st.title("This is my first API toy project")
st.subheader("Basic Caculator")

x = st.text_area('x 숫자 입력') # number_input하면, format 등 지정 번거로움 -> api에서 pydantic 검증을 통해 float로 인풋됨
operator = st.selectbox("부등호", ("+", "-", "/", "*"))
y = st.text_area('y 숫자 입력')

info_dict = {'x':x, 'y':y, 'operator':operator}

# it returns a True if the button was clicked on the last run of the app, and False otherwise.
if st.button('Calculate'):
    result = requests.post(url='http://127.0.0.1:8000/calculator', data=json.dumps(info_dict), verify=False)
    
    st.subheader(f"result: {result.text}")
