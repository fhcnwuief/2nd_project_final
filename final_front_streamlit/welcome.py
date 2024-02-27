import streamlit as st
from PIL import Image
import io

background_style = """
    <style>
    body {
        background-color: #f0f0f0; /* 원하는 배경색으로 변경하세요 */
    }
    </style>
"""

# Streamlit 앱 시작
st.markdown(background_style, unsafe_allow_html=True)

def load_image(image_file):
    img = Image.open(image_file)
    return img


st.markdown(
    f'<div style="display: flex; justify-content: center;"><h1>{"향수 찾기 프로그램"}</h1></div>',
    unsafe_allow_html=True
)
col2 = st.columns(2)

image_path = '/Users/changhoon/Documents/DataScience/project/perfume/perfume_streamlit/제목을-입력해주세요_-002.png'
img = load_image(image_path)

# 이미지를 중앙에 배치하고 Streamlit으로 출력
buffered = io.BytesIO()
img.save(buffered, format="PNG")
st.image(buffered, width=1000, use_column_width=True, caption="main_thumbnail")

''
''

st.markdown(
                f'<p style="text-align: center; font-weight: bold; ">향수 추천 프로그램 소개</p>',
                unsafe_allow_html=True
                )
''
''
''

'여러분을 위한 최적의 향수를 찾아드립니다! 우리의 향수 추천 프로그램은 개인의 선호를 고려하여, 다양한 향수 중에서 딱 맞는 향수를 찾아드립니다.'
'향수는 우리의 개성을 반영하는 중요한 요소 중 하나입니다.'
'그래서 우리는 자연어 처리 기술과 머신 러닝 알고리즘을 활용하여, 사용자의 기호와 취향을 파악하여 최적의 향수를 추천해드립니다.'

'우리의 향수 추천 프로그램은 다음과 같은 특징을 가지고 있습니다:'

':thumbsup: **맞춤형 추천** '
' 사용자의 선호하는 향을 기반으로, 다양한 향수 중에서 가장 어울리는 향수를 찾아드립니다.'

':thumbsup: **다양한 브랜드와 향수**'
'다양한 브랜드와 수많은 향수 중에서 선택할 수 있습니다. 각 브랜드와 향수의 특징을 알려드리며, 가장 적합한 향수를 추천해드립니다.'

':thumbsup: **정확한 추천** '
'자연어 처리 기술과 머신 러닝 알고리즘을 활용하여, 사용자의 단어 선택과 문맥을 분석하여 정확한 추천을 제공합니다.'

':thumbsup: **간편한 사용** '
'사용자 친화적인 인터페이스로, 손쉽게 향수 추천을 받을 수 있습니다. 몇 가지 간단한 질문에 답하면, 최적의 향수가 나타납니다.'
''
''

'지금 바로 우리의 향수 추천 프로그램을 통해 나만의 특별한 향수를 찾아보세요! '
'개성을 반영하는 향수로 더욱 멋진 일상을 시작해보세요!!'