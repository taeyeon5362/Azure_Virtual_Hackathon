import streamlit as st
import pandas as pd
import numpy as np



#제목
st.title('A 프로그램')
st.subheader('프로그램 설명  |  날짜 : 2022.01.01 ~ 2022.01.02  |  용량 : 2.03 GB  |  카테고리 : A ')
st.subheader(' ')
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
st.subheader(' ')

ai_0 = ai_0.groupby('timestamp').sum()
aies_0 = ai_0.index.tolist()
option = st.selectbox('Select_0',(aies_0))

ai_data_0 = ai_0.loc[(ai_0.index == option)]
ai_index_0 = ai_data_0.index.tolist()
st.line_chart(ai_data_0.loc[ai_index_0[0]], use_container_width=True)
