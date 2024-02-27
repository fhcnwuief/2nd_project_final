import streamlit as st
import streamlit.components.v1 as html
from st_pages import Page, Section, show_pages, add_page_title
from  PIL import Image
import pydeck as pdk
from urllib.error import URLError
import pandas as pd
import time
import numpy as np
import webbrowser
import os
from ast import literal_eval
from result1 import display_result
from result2 import display_result2
from result3 import display_result3




df = pd.read_csv('/Users/changhoon/Documents/DataScience/project/perfume/perfume_streamlit/cate_note.csv')
# st.dataframe(df)
category = ["citrus_smells","fruits_vegetables_and_nuts", "flowers","white_flowers","greens_herbs_and_fougeres","spices","sweets_and_gourmand_smells","woods_and_mosses","resins_and_balsams",
            "musk_amber_animalic_smells","beverages","netural_and_synthetic_popular_and_weird"]  # 카테고리 목록을 적절히 변경하세요
df['notes'] = df['notes'].apply(literal_eval)
note8 = df['notes'][7]
note1 = df['notes'][0]
note10 = df['notes'][9]

# _, _, _, col, _, _, _ = st.columns([1]*6+[1.18])
st.markdown(
    f'<div style="display: flex; justify-content: center;"><h1>{"이향 어때?"}</h1></div>',
    unsafe_allow_html=True
)
''
''
selected_options = st.multiselect('Select options:', category)
''
''       
if "citrus_smells" in selected_options:
    selected_values = st.multiselect('topnote를 고르세요', note1 )
elif "woods_and_mosses" in selected_options:
    selected_values = st.multiselect('topnote를 고르세요', note8 )
elif "musk_amber_animalic_smells" in selected_options:
    selected_values = st.multiselect('topnote를 고르세요', note10 )
else:
    st.write('No options selected.')
''
''  
if "citrus_smells" in selected_options:
    selected_values = st.multiselect('middlenote를 고르세요', note1 )
elif "woods_and_mosses" in selected_options:
    selected_values = st.multiselect('middlenote를 고르세요', note8 )
elif "musk_amber_animalic_smells" in selected_options:
    selected_values = st.multiselect('middlenote를 고르세요', note10 )
else:
    st.write('No options selected.')
  
''    
''         
if "citrus_smells" in selected_options:
    selected_values = st.multiselect('basenote를 고르세요', note1 )
elif "woods_and_mosses" in selected_options:
    selected_values = st.multiselect('basenote를 고르세요', note8 )
elif "musk_amber_animalic_smells" in selected_options:
    selected_values = st.multiselect('basenote를 고르세요', note10 )
else:
    st.write('No options selected.')
''
''
''

def open_path(path):
    webbrowser.open(path)
path = r'http://localhost:8502/'


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
        


# 전역 스택 변수를 선언합니다.
page_stack = []


def main():
    button_style = """
    position: fixed;
    bottom: 10px;
    right: 10px;
    """
    ''
    st.header("When you're done, press 'Done' button")
    global page_stack  # 전역 스택 변수 사용

    if not page_stack or page_stack[-1] == "main":
        if st.button("Done"):
            st.text('start recommending . . .')
            spinner()
            page_stack.append("result")
            
    if page_stack and page_stack[-1] == "result":
        if "citrus_smells" in selected_options:
            display_result()
        elif "woods_and_mosses" in selected_options:
            display_result2()
        elif "musk_amber_animalic_smells" in selected_options:
            display_result3()
    
    if page_stack and page_stack[-1] == "result":
        if st.button("뒤로 가기"):
            page_stack.pop()

        

# 이전에 제공한 spinner() 함수와 display_result() 함수

if __name__ == "__main__":
    main()