import streamlit as st
import streamlit.components.v1 as html
from streamlit_option_menu import option_menu
from  PIL import Image
import pydeck as pdk
from urllib.error import URLError
import pandas as pd
import time
import numpy as np
import webbrowser
import os


category = ["카테고리1", "카테고리2", "카테고리3"]  # 카테고리 목록을 적절히 변경하세요



_, _, _, col, _, _, _ = st.columns([1]*6+[1.18])
title = col.title('perfume')
''
''

st.multiselect('당신이 희망하는 향을 고르세요', category)
''
''       
st.multiselect('topnote를 고르세요', category)
''       
''
st.multiselect('middlenote를 고르세요', category)
''    
''   
st.multiselect('basenote를 고르세요', category)        
''
''
st.slider('가격', 0, 300, (0,300))
''
''

def open_path(path):
    webbrowser.open(path)

path = r'C:/Users/godgr/Documents/Datascience/source/2차프로젝트/streamlit/welcome.py'


def spinner():
    with st.spinner("향수를 찾고 있습니다"):
   

        time.sleep(3)  # 첫 번째 기능 실행 시뮬레이션
        latest_iteration = st.empty()
        bar = st.progress(0)

        for i in range(100):
  # Update the progress bar with each iteration.
                    latest_iteration.text(f'로딩중 {i+1}')
                    bar.progress(i)
                    time.sleep(0.02)
  # 0.05 초 마다 1씩증가
        st.success('향수찾기가 완료되었습니다', icon="✅")
        open_path(path)

_, _, _, col, _, _, _ = st.columns([1] * 6 + [1.1])
clicked = col.button('완료')

if clicked:
 spinner()











