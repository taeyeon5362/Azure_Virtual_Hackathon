import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


#제목
st.title('A 프로그램')
st.header('프로그램 설명  |  날짜 : 2021.07.10 ~ 2021.07.11  |  용량 : 2.03 GB  |  카테고리 : A ')
st.subheader(' ')
st.subheader(' ')

#데이터 불러오기


time = pd.read_csv('./csv/validation_time.csv', encoding='cp949')
time.set_index = time['timestamp']

data_1 = pd.read_csv('./csv/validation_data_1.csv', encoding='cp949')
data_1.set_index = data_1['timestamp']

data_2 = pd.read_csv('./csv/validation_data_2.csv', encoding='cp949')
data_2.set_index = data_2['timestamp']



#ai 그래프

st.header('보안 데이터 수치')
st.subheader(' ')


st.subheader('시간별 데이터 비교')

time = time.groupby('timestamp').sum()
times = time.index.tolist()
option = st.selectbox('Select Time',(times))

time_data = time.loc[(time.index == option)]
time_index = time_data.index.tolist()
st.line_chart(time_data.loc[time_index[0]], use_container_width=True)


st.subheader('데이터별 시간 데이터 비교')
st.subheader(' ')


st.write('시간별 비교')

data_1 = data_1.groupby('timestamp').sum()
datas_1 = data_1.index.tolist()
option = st.selectbox('Select Data 1',(datas_1))

data_data_1 = data_1.loc[(data_1.index == option)]
data_index_1 = data_data_1.index.tolist()
st.line_chart(data_data_1.loc[data_index_1[0]], use_container_width=True)

st.subheader(' ')
st.write('한시간 비교')

data_2 = data_2.groupby('timestamp').sum()
datas_2 = data_2.index.tolist()
option = st.selectbox('Select Data 2',(datas_2))

data_data_2 = data_2.loc[(data_2.index == option)]
data_index_2 = data_data_2.index.tolist()
st.line_chart(data_data_2.loc[data_index_2[0]], use_container_width=True)

st.subheader(' ')
st.header('변수 중요도')
st.subheader(' ')

fin = pd.read_csv('./csv/validation_fin.csv')
#st.dataframe(val)
fin_chart = px.bar(fin, x='timestamp', y='fin')
st.plotly_chart(fin_chart)
