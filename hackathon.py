import streamlit as st
import pandas as pd
import numpy as np



#제목
st.title('A 프로그램')
st.subheader('프로그램 설명  |  날짜 : 2022.01.01 ~ 2022.01.02  |  용량 : 2.03 GB  |  카테고리 : A ')

#데이터 불러오기
ai_0 = pd.read_csv('./csv/val_10_0_00.csv', encoding='cp949')
ai_0.set_index = ai_0['timestamp']

#ai
st.subheader('보안 데이터 수치')


ai_0 = ai_0.groupby('timestamp').sum()
aies_0 = ai_0.index.tolist()
option = st.selectbox('Select_0',(aies_0))

ai_data_0 = ai_0.loc[(ai_0.index == option)]
ai_index_0 = ai_data_0.index.tolist()
st.line_chart(ai_data_0.loc[ai_index_0[0]], use_container_width=True)
