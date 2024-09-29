import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import requests 

st.title('요청자, 처리자간의 통계')

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

#import numpy as np 
#rg=df.groupby('request_user').count()
#pg=df.groupby('prediction_model').count()
#x_rg = np.arange(len(rg))+0.25
#x_pg = np.arange(len(pg))
#plt.bar(x_rg,rg['num'].values,width=0.2,color='red')
#plt.bar(x_pg,pg['num'].values,width=0.2,color='blue')
#plt.xticks(x_rg, rg.index)
#plt.legend(('REQ','PRED'))
#plt.xticks(rotation = 45)
#plt.title("Requests and Predict difference")
#plt.xlabel("request user")
#plt.ylabel("Number of Requests and predcit")

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

# 결측치 처리
cdf['prediction_model'].fillna("nothin",inplace=True)

# 내가 요청하고 내가처리한것, 남이처리한것 구분
cdf.loc[(cdf['prediction_model']!=cdf['request_user']) & (cdf['prediction_model']!= 'nothin'),'prediction_model']="another"
cdf.loc[(cdf['prediction_model']==cdf['request_user']),'prediction_model']="me"

# 요청에 따라 다른 사람이 처리한것, 내가 한것, 아무 처리도 못받은 것으로 그룹짓기
ccdf=cdf.groupby(['request_user','prediction_model']).size()

# 그래프 그리기 
import numpy as np
unstacked = ccdf.unstack()
x_rg=np.arange(len(unstacked.index))
unstacked.plot(kind='bar',figsize=(10, 6), width=0.8)
plt.xticks(x_rg)

plt.xlabel('request_user')
plt.ylabel('predict_models count per request_user ')

#화면 출력 
st.pyplot(plt)

# 출력 결과 해석 
st.subheader('그래프에서 x축은 request_user를 뜻하고, y축은 요청자의 데이터에 대해 자신이 처리한것(me) , 다른사람의 처리 한 것 (another)  또 처리되지않은 요청수(nothin) 에 대해 출력한 결과이다')

