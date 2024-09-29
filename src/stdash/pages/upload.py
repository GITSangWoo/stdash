import streamlit as st
import requests
from io import StringIO


menu = ['이미지 업로드', '핫도그 사진 판별기']

choice = st.sidebar.selectbox('메뉴',menu)

st.markdown("STEP2 upload_file🎈")
st.sidebar.markdown("upload_file🎈")

st.title('upload_file')

url = 'http://43.202.66.118:8077/upload_file'
uploaded_file = st.file_uploader("Choose a file")

