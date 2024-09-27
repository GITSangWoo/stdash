import streamlit as st
import pandas as pd 
import datetime as dt 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.dates as dates

st.title('multi page 1')

def load_data():
    url = 'http://43.202.66.118:8077/all'
    r = requests.get(url)
    d = r.json()
    return d

data = load_data()
df = pd.DataFrame(data)

rdf=df[['request_time','request_user']]
rdf['request_time']=pd.to_datetime(rdf['request_time'])
rdf['request_time']=rdf['request_time'].dt.strftime('%m-%d %H')
plt.bar(rdf['request_user'],rdf['request_time'])
plt.xticks(rotation=90)


pdf=df[['prediction_model','prediction_time']]
pdf['prediction_time']=pd.to_datetime(pdf['prediction_time'])
pdf['prediction_time']=pdf['prediction_time'].dt.strftime('%m-%d %H')
plt.bar(pdf['prediction_model'],pdf['prediction_time'])
plt.xticks(rotation=90)
