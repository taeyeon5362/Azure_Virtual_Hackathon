import streamlit as st
import pandas as pd
import numpy as np



#제목
st.title('A 프로그램')
st.subheader('프로그램 설명  |  날짜 : 2022.01.01 ~ 2022.01.02  |  용량 : 2.03 GB  |  카테고리 : A ')
st.subheader(' ')
st.subheader(' ')

#데이터 불러오기


time = pd.read_csv('./csv/validation_time.csv', encoding='cp949')
time.set_index = time['timestamp']

data_1 = pd.read_csv('./csv/validation_data_1.csv', encoding='cp949')
data_1.set_index = data_1['timestamp']





#ai 그래프

st.subheader('보안 데이터 수치')
st.subheader(' ')


st.write('시간별 데이터 비교')

time = time.groupby('timestamp').sum()
times = time.index.tolist()
option = st.selectbox('Select Time',(times))

time_data = time.loc[(time.index == option)]
time_index = time_data.index.tolist()
st.line_chart(time_data.loc[time_index[0]], use_container_width=True)


st.write('데이터별 시간 데이터 비교')

data_1 = data_1.groupby('timestamp').sum()
datas_1 = data_1.index.tolist()
option = st.selectbox('Select Data 1',(datas_1))

data_data_1 = data_1.loc[(data_1.index == option)]
data_index_1 = data_data_1.index.tolist()
st.line_chart(data_data_1.loc[data_index_1[0]], use_container_width=True)



