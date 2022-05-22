# SAI-board

변수 중요도

fin_chart = alt.Chart(fin).mark_bar().encode(x=alt.X('data', sort=None), y='fin', )
st.altair_chart(fin_chart, use_container_width=True)

