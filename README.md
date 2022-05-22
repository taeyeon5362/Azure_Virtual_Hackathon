# SAI-board

변수 중요도

fin_chart = alt.Chart(fin).mark_bar().encode(x=alt.X('data', sort=None), y='fin', )
st.altair_chart(fin_chart, use_container_width=True)




시간별 비교

time = time.groupby('timestamp').sum()
times = time.index.tolist()
option = st.selectbox('Select Time',(times))

time_data = time.loc[(time.index == option)]
time_index = time_data.index.tolist()
st.line_chart(time_data.loc[time_index[0]], use_container_width=True)
