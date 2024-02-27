import streamlit as st
import pandas as pd
from PIL import Image
import os
from bs4 import BeautifulSoup
import lxml
import requests
import io
import math


# 1달러는 지금 몇원일지...?!
def korean_won():
    r = requests.get('https://finance.naver.com/marketindex/?tabSel=exchange#tab_section')
    soup = BeautifulSoup(r.content, 'lxml')

    get_current = soup.find("span", class_="value").get_text()
    get_current = get_current.replace(',', '')
    get_current = float(get_current)

    return get_current


# 이미지 불러오는 함수 
def load_image(image_file):
    img = Image.open(image_file)
    return img



def display_result():
    st.markdown(
    f'<div style="display: flex; justify-content: center;"><h1>{"Recommendation result"}</h1></div>',
    unsafe_allow_html=True)
    
    st.markdown(
                f'<p style="text-align: center; font-size: 24px;">Results are here! I will show you the 3 most similar ones</p>',
                unsafe_allow_html=True
                )


    df = pd.read_csv('/Users/changhoon/Documents/DataScience/project/perfume/perfume_streamlit/cat1_result.csv')
    df1 = df[['name','brand','price']]
    # st.dataframe(df)
    num_columns = len(df1.columns)
    col_count = 0
    columns = st.columns(num_columns)

    
    money_list = []
    won = korean_won()
    for price in df1['price']:
        money = won * price
        money = math.trunc(money)
        money = f'{money:,}'
        money_list.append('₩ '+ money)
        
    df1['price'] = pd.DataFrame(money_list)
    
    for i in range(len(df)):
        with columns[col_count]:
            image = '/Users/changhoon/Documents/DataScience/project/perfume/perfume_streamlit/images/' + str(df['pk'][i]) + '.jpg'
            img = load_image(image)
            # image_file = 이미지 파일이 들어있는 변수
            # st.image(img,width=200)
            # 이미지를 중앙에 배치하고 Streamlit으로 출력
            buffered = io.BytesIO()
            img.save(buffered, format="PNG")
            st.image(buffered, use_column_width=True,caption=df['name'][i])   
            
            # Write DataFrame contents as text
            row_data = df1.iloc[i]
            for col_name, value in row_data.items():
                # st.text(f"{col_name}: {value}")
                st.markdown(
                f'<p style="text-align: center;">{col_name}: {value}</p>',
                unsafe_allow_html=True
                )
            
        col_count = (col_count + 1) % num_columns