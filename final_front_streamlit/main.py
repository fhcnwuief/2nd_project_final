import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title

# add_page_title() # By default this also adds indentation

# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
    [
        Page("welcome.py", "welcome", ":wave:"),
        Page("ui.py", "향수찾기", ":mag:"),
    ]
)
st.header(' Welcome to our program! ')
''
''
st.subheader(' We hope that our program will give you the results you desire.')
''
''
''
st.subheader(' First, move to "welcome" and read Introduction !')