import streamlit as st
import pandas as pd


#타이틀 
st.title("2022 Azure Virtual Hackathon 마이크로소프트 해커톤")

#헤더 
st.header("제 2분야 AI")

#중간
st.subheader("streamlit의 이해")

#글자 넣기 
st.text("버튼 만들기")

if st.button("click button"):
    st.write("Data Loading..")

if st.button("success"):
    st.success("Successful!")
    
if st.button("error"):
    st.error("error!")

if st.button("information"):
    st.info("Information")

if st.button("warning"):
    st.warning("This is a warning")

input = st.text_input(label = "message", value="입력하시오",max_chars=10, help='10글자 이상 입력x')
st.write(input)


checkbox_btn = st.checkbox('checkbox Button')

if checkbox_btn:
    st.write('Great!')

#왼쪽 사이드바 
add_selectbox = st.sidebar.selectbox("MS Azure Hackathon Select Box", ("DevOps", "AI", "Gaming"))

#드랍다운 선택
sel = st.selectbox("선택하세요. ",
                   ["사과","바나나","오렌지","멜론","수박"])
st.write("당신이 선택한 과일은 ",sel,"입니다. ")

#드랍다운 다중 선택 
selectbox_mul = st.multiselect("선택하세요. ",
                          ("DevOps_1","DevOps_2",
                           "AI_1","AI_2",
                           "Gaming_1","Gaming_2"))
st.write(len(selectbox_mul),"가지를 선택했습니다. ")



from sklearn.datasets import load_iris
iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['target'] = iris['target']
iris_df['target'] = iris_df['target'].apply(lambda x: 'setosa' if x == 0 else ('versicolor' if x == 1 else 'virginica'))

#전체 리턴 
st.table(iris_df.head())

#스크롤 데이터 관찰 
st.dataframe(iris_df)
st.write(iris_df)


#슬라이더
level = st.slider("레벨을 선택하세요.",1,100)
st.write("당신이 선택한 레벨은 ",level,"입니다.")


#날짜입력
import datetime
today = st.date_input("날짜를 선택하세요.", datetime.datetime.now())
the_time = st.time_input("시간을 입력하세요", datetime.time())
st.write("오늘의 날짜는",today,"입니다.")
st.write("지금 시간은",the_time,"입니다.")



st.text(" ")
st.text(" ")
st.text(" ")
st.text(" ")
st.text(" ")
st.text(" ")


st.subheader("대시보드 변수 구상")

from PIL import Image
img = Image.open("/Users/gimtaeyeon/ai.png")
st.image(img, width=800,caption="AI 사진 ")

st.markdown("전체적인 인공지능 대시보드")

st.markdown("- 위협이 되는 이유 \n"
            "  - 하드웨어 \n"
            "  - 소프트웨어 \n")
st.markdown("- 인공지능 사용시 효과 \n"
            "  - 이용 시 \n"
            "  - 이용 안 할 시 \n")
st.markdown("- 인공지능 이용 및 감지 \n"
            "  - A  case \n"
            "  - B  case \n"
            "  - C  case \n"
            "  - D  case \n")

st.markdown("- 인공지능으로 발견할 수 있는 위협 종류 \n"
            "  - A dan \n"
            "  - B dan \n"
            "  - C dan \n"
            "  - D dan \n")

st.markdown("- 사용 분야 (원그래프) \n"
            "  - A \n"
            "  - B \n"
            "  - C \n"
            "  - D \n")


st.markdown("인공지능 사용 시 결과 대시보드")

st.markdown("- 인공지능을 사용할 프로그램 명 \n"
            "  - 인공지능 실행 날짜(기간) 등 간단한 프로그램을 돌리는 조건 \n"
            "  - 프로그램 용량, 프로그램 카테고리 등 간단한 프로그램 설명 \n"
            "  - 사용 전 보안 정도 \n"
            "  - 사용 후 기간별 보안 정도 (막대그래프) \n"
            "  - 관측된 위협 정보 (항목) \n"
            "  - 프로그램 보완 사항 \n")
            


st.subheader("스웜러닝 이란?")

st.markdown("1. 스웜러닝\n"
            "   1. 스웜러닝의 효과 \n"
            "   2. 스웜러닝 \n"
            "2. 스웜런닝 이용시 얼마나 효과가 있는가 \n"
            "   1. 이용 안할시 \n"
            "   2. 이용 시 \n"
            "3. item 3\n")


