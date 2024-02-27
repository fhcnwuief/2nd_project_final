import streamlit as st
import streamlit.components.v1 as html
from streamlit_option_menu import option_menu
from  PIL import Image
import pydeck as pdk
from urllib.error import URLError
import pandas as pd
import time
import numpy as np

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)