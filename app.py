import streamlit as st
import psutil as ps
import pandas as pd
import numpy as np



st.title("Sistema de Gerenciamento de Processos")
DATE_COLUMN = 'date/time'
DATA_URL=('https://s3-us-west-2.amazonaws.com/''streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data=pd.read_csv(DATA_URL, nrows=nrows)
    lowercase= lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')
hist_values=np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

hour_to_filter=st.slider('hour',0,23,17)
filtered_data= data[data[DATE_COLUMN].dt.hour==hour_to_filter]

st.subheader('Map of all pickups at %s:00' %hour_to_filter)
st.map(filtered_data)







st.write("Hello World")
teste=ps.cpu_times()
#scputimes(user=3961.46, nice=169.729, system=2150.659, idle=16900.540, iowait=629.59, irq=0.0, softirq=19.42, steal=0.0, guest=0, guest_nice=0.0)
st.write(teste.user)