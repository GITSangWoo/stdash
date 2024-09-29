import streamlit as st
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.dates as dates
import requests
import plotly.express as px

st.markdown("STEP2 multi page 1 🎈")
st.sidebar.markdown("Multi page 1 🎈")

st.title('n77 요청수와 처리수 및 유저별 처리수')

def load_data():
    url = 'http://43.202.66.118:8077/all'
    r = requests.get(url)
    d = r.json()
    return d

data = load_data()
df = pd.DataFrame(data)


# 요청시간 예측시간 datetime 형식으로 바꾸고 포맷 바꾸기
df['request_time']=pd.to_datetime(df['request_time'])
df['prediction_time']=pd.to_datetime(df['prediction_time'])
df['request_stime']=df['request_time'].dt.strftime("%Y-%m-%d %H")
df['prediction_stime']=df['prediction_time'].dt.strftime("%Y-%m-%d %H")

# 요청 유저와 시간 데이터 프레임
rdf=df[['num','request_time','request_user','request_stime']]

# 예측한 모델(사람)과 예측한 시간
pdf=df[['num','prediction_time','prediction_model','prediction_stime']]
pdf=pdf[pdf['prediction_model'].str.contains(r'^n')]

# pdf 와 rdf를 merge
cdf=pd.merge(rdf,pdf,how='left',on='num')

# 다중 칼럼 그룹화
import numpy as np
g12df=cdf.groupby(['request_user','prediction_model']).size()
unstacked = g12df.unstack()
fig1 = px.pie(unstacked, values='n04', names='n77', title='Example Pie Chart')
st.plotly_chart(fig1)
