import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import requests 

st.title('CNN JOB MON')

def load_data():
    url = 'http://43.202.66.118:8077/all'
    r = requests.get(url)
    d = r.json()
    return d 

data = load_data()
df = pd.DataFrame(data)
#df

# TODO 
# request_time, prediction_time 이용해 '%Y-%m-%d %H' 형식
# 시간별 GROUPBY COUNT 하여 plt 차트 그려보기 
#df['request_time'] = pd.to_datetime(df['request_time'])
#df['request_time']=df['request_time'].dt.strftime('%Y-%m-%d %H')
#count=df.groupby('request_time').size()
#plt.bar(count.index,count.values)
#plt.plot(count.index,count.values,color='red',linestyle='-',marker='o')
#plt.plot(count.index,count.values,color='red',linestyle='-',marker='o')

import numpy as np 
rg=df.groupby('request_user').count()
pg=df.groupby('prediction_model').count()
x_rg = np.arange(len(rg))+0.25
x_pg = np.arange(len(pg))
plt.bar(x_rg,rg['num'].values,width=0.2,color='red')
plt.bar(x_pg,pg['num'].values,width=0.2,color='blue')
plt.xticks(x_rg, rg.index)
plt.legend(('REQ','PRED'))
plt.xticks(rotation = 45)
plt.title("Requests and Predict difference")
plt.xlabel("request user")
plt.ylabel("Number of Requests and predcit")

#화면 출력 
st.pyplot(plt)

