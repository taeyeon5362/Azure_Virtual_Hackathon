import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import altair as alt    
import plotly.express as px


#제목
st.title('A 프로그램')
st.subheader('프로그램 설명  |  날짜 : 2022.01.01 ~ 2022.01.02  |  용량 : 2.03 GB  |  카테고리 : A ')
st.subheader(' ')
st.subheader(' ')

#데이터 불러오기
ai_0 = pd.read_csv('./csv/val_10_0_00.csv', encoding='cp949')
ai_0.set_index = ai_0['timestamp']

ai_1 = pd.read_csv('./csv/val_10_0_01.csv', encoding='cp949')
ai_1.set_index = ai_1['timestamp']

ai_2 = pd.read_csv('./csv/val_10_0_02.csv', encoding='cp949')
ai_2.set_index = ai_2['timestamp']

ai_3 = pd.read_csv('./csv/val_10_0_03.csv', encoding='cp949')
ai_3.set_index = ai_3['timestamp']

ai_4 = pd.read_csv('./csv/val_10_0_04.csv', encoding='cp949')
ai_4.set_index = ai_4['timestamp']

ai_5 = pd.read_csv('./csv/val_10_0_05.csv', encoding='cp949')
ai_5.set_index = ai_5['timestamp']

ai_6 = pd.read_csv('./csv/val_10_0_06.csv', encoding='cp949')
ai_6.set_index = ai_6['timestamp']

ai_7 = pd.read_csv('./csv/val_10_0_07.csv', encoding='cp949')
ai_7.set_index = ai_7['timestamp']

ai_8 = pd.read_csv('./csv/val_10_0_08.csv', encoding='cp949')
ai_8.set_index = ai_8['timestamp']

ai_9 = pd.read_csv('./csv/val_10_0_09.csv', encoding='cp949')
ai_9.set_index = ai_9['timestamp']

ai_10 = pd.read_csv('./csv/val_10_0_10.csv', encoding='cp949')
ai_10.set_index = ai_10['timestamp']




#ai 그래프

st.subheader('보안 데이터 수치')
st.subheader(' ')

ai_0 = ai_0.groupby('timestamp').sum()
aies_0 = ai_0.index.tolist()
option = st.selectbox('Select_0',(aies_0))

ai_data_0 = ai_0.loc[(ai_0.index == option)]
ai_index_0 = ai_data_0.index.tolist()
st.line_chart(ai_data_0.loc[ai_index_0[0]], use_container_width=True)


ai_1 = ai_1.groupby('timestamp').sum()
aies_1 = ai_1.index.tolist()
option = st.selectbox('Select_1',(aies_1))

ai_data_1 = ai_1.loc[(ai_1.index == option)]
ai_index_1 = ai_data_1.index.tolist()
st.line_chart(ai_data_1.loc[ai_index_1[0]], use_container_width=True)


ai_2 = ai_2.groupby('timestamp').sum()
aies_2 = ai_2.index.tolist()
option = st.selectbox('Select_2',(aies_2))

ai_data_2 = ai_2.loc[(ai_2.index == option)]
ai_index_2 = ai_data_2.index.tolist()
st.line_chart(ai_data_2.loc[ai_index_2[0]], use_container_width=True)


ai_3 = ai_3.groupby('timestamp').sum()
aies_3 = ai_3.index.tolist()
option = st.selectbox('Select_3',(aies_3))

ai_data_3 = ai_3.loc[(ai_3.index == option)]
ai_index_3 = ai_data_3.index.tolist()
st.line_chart(ai_data_3.loc[ai_index_3[0]], use_container_width=True)


ai_4 = ai_4.groupby('timestamp').sum()
aies_4 = ai_4.index.tolist()
option = st.selectbox('Select_4',(aies_4))

ai_data_4 = ai_4.loc[(ai_4.index == option)]
ai_index_4 = ai_data_4.index.tolist()
st.line_chart(ai_data_4.loc[ai_index_4[0]], use_container_width=True)


ai_5 = ai_5.groupby('timestamp').sum()
aies_5 = ai_5.index.tolist()
option = st.selectbox('Select_5',(aies_5))

ai_data_5 = ai_5.loc[(ai_5.index == option)]
ai_index_5 = ai_data_5.index.tolist()
st.line_chart(ai_data_5.loc[ai_index_5[0]], use_container_width=True)


ai_6 = ai_6.groupby('timestamp').sum()
aies_6 = ai_6.index.tolist()
option = st.selectbox('Select_6',(aies_6))

ai_data_6 = ai_6.loc[(ai_6.index == option)]
ai_index_6 = ai_data_6.index.tolist()
st.line_chart(ai_data_6.loc[ai_index_6[0]], use_container_width=True)


ai_7 = ai_7.groupby('timestamp').sum()
aies_7 = ai_7.index.tolist()
option = st.selectbox('Select_7',(aies_7))

ai_data_7 = ai_7.loc[(ai_7.index == option)]
ai_index_7 = ai_data_7.index.tolist()
st.line_chart(ai_data_7.loc[ai_index_7[0]], use_container_width=True)


ai_8 = ai_8.groupby('timestamp').sum()
aies_8 = ai_8.index.tolist()
option = st.selectbox('Select_8',(aies_8))

ai_data_8 = ai_8.loc[(ai_8.index == option)]
ai_index_8 = ai_data_8.index.tolist()
st.line_chart(ai_data_8.loc[ai_index_8[0]], use_container_width=True)


ai_9 = ai_9.groupby('timestamp').sum()
aies_9 = ai_9.index.tolist()
option = st.selectbox('Select_9',(aies_9))

ai_data_9 = ai_9.loc[(ai_9.index == option)]
ai_index_9 = ai_data_9.index.tolist()
st.line_chart(ai_data_9.loc[ai_index_9[0]], use_container_width=True)
