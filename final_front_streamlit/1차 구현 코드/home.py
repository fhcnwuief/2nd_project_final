import streamlit as st
import streamlit.components.v1 as html
from streamlit_option_menu import option_menu
from  PIL import Image
import pydeck as pdk
from urllib.error import URLError
import pandas as pd
import time
import numpy as np

def home():
    st.title("홈 페이지")
    st.write("이곳은 홈 페이지입니다.")
    
def profile():
    st.title("프로필 페이지")
    st.write("이곳은 프로필 페이지입니다.")
    
def settings():
    st.title("설정 페이지")
    st.write("이곳은 설정 페이지입니다.")

def main():
    with st.sidebar:
        choose = option_menu("MY Perfume", ['home',"Choose my perfume", "Recommended perfume"],
                         icons=['bi bi-search-heart', 'bi bi-hand-thumbs-up'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#ead1dc"},
        "icon": {"color": "#F44336", "font-size": "30px"}, 
        "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#ead1dc"},
        "nav-link-selected": {"background-color": "#f8f1f4"},
    }
    )

    if option_menu == "home":
        home()
    elif option_menu == "Choose my perfume":
        profile()
    elif option_menu == "Recommended perfume":
        settings()

if __name__ == "__main__":
    st.set_page_config(page_title="home", layout="wide")
    main()