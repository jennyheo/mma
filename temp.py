# -*- codi     ng: utf-8 -*-

import streamlit as st
import pandas as pd
import pyarrow as pa

st.set_page_config(layout="wide")
#.streamlit/config.toml 파일에서 maincolor 지정 : 파란색

st.subheader('병역처분결과에 대해 알려드립니다')

with st.expander('😄 알려드립니다'):
  st.write('병역판정검사(입영판정검사) 결과지 내용에 대해 궁금한 사항을 안내합니다.')
  st.image('https://mma.go.kr/download/visual/CAIS_HPIS_202412020402149250.jpg', width=250)

#사이드바 옵션
#st.sidebar.header('입력')
#user_name = st.sidebar.selectbox('병역처분 결과를 입력하세요', ['','현역입영대상','사회복무요원소집대상','전시근로역','병역면제','재검대상'])
#user_emoji = st.sidebar.selectbox('검사결과 중 어떤 항목이 궁금하신가요?', ['', '체질량지수','혈압','색각','AST','ALT','간염','Gloucoss'])
#user_food = st.sidebar.selectbox('가장 좋아하는 음식은?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

#탭메뉴의 글자크기 지정
css = ''' 
<style>
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size:15px;
    }

	.stTabs [data-baseweb="tab-list"] {
		gap: 2px;
    }
	.stTabs [data-baseweb="tab"] {
		height: 30px;
        white-space: pre-wrap;
		background-color: #ffffff;
		border-radius: 4px 4px 0px 0px;
		gap: 1px;
		padding-top: 10px;
          padding-right: 10px;
		padding-bottom: 10px;
          padding-left: 10px;
    }
	.stTabs [aria-selected="true"] {
  		#background-color: #0000ff;
          #color: #FFFFFF;
	}
</style>
'''

tab1, tab2, tab3 = st.tabs(['병역처분','검사참고치','바로가기']) #탭메뉴 가로형

st.markdown(css, unsafe_allow_html=True)

with tab1:
     st.subheader('병역처분결과를 입력하세요', divider=True)
     #st.markdown("##### 병역처분결과를 입력하세요")
     #st.divider()
     user_name = st.selectbox('', ['','현역입영대상','사회복무요원소집대상','전시근로역','병역면제','재검대상'])


     if user_name != '':
          #st.subheader(', divider=True)
          st.markdown(f"#### 👉 {user_name} 안내입니다")
     else:
          st.markdown('')

     if user_name == '현역입영대상' :
          st.write('1-3급은 현역입영대상입니다')
     elif user_name == '사회복무요원소집대상' :
          st.write('4급은 사회복무요원 소집 대상입니다')
     elif user_name == '전시근로역' :
          st.write('5급은 전시근로역대상입니다')
     elif user_name == '병역면제' :
          st.write('6급은 병역이 면제됩니다')
     elif user_name == '재검대상' :
          st.write('7급 재검대상은 치유기간 이후 다시 재검을 받으셔야 합니다')
     else: 
          st.write('')

with tab2:
     st.subheader('검사결과 중 어떤 항목이 궁금하신가요?', divider=True)

     col1, col2, col3 = st.columns([2,1,1])
     col4, col5, col6, col7, col8 = st.columns([1,1,1,1,1])
     col9, col10, col11 = st.columns([1,1,1])

     if 'kkk' not in st.session_state:
          st.session_state['kkk'] = '체질량지수'
     
     with st.container():
          with col1:
               but1=st.button('체질량지수', use_container_width=True)
               if but1:
                    st.session_state['kkk'] = '체질량지수'
          with col2:
               but2=st.button('혈압', use_container_width=True)
               if but2:
                    st.session_state['kkk'] = '혈압'
          with col3:
               but3=st.button('색각', use_container_width=True)
               if but3:
                    st.session_state['kkk'] = '색각'
     with st.container():
          with col4:
               but4=st.button('AST', use_container_width=True)
               if but4:
                    st.session_state['kkk'] = 'AST'
          with col5:
               but5=st.button('ALT', use_container_width=True)
               if but5:
                    st.session_state['kkk'] = 'ALT'
          with col6:
               but6=st.button('간염', use_container_width=True)
               if but6:
                    st.session_state['kkk'] = '간염'
          with col7:
               but7=st.button('Glucoss', use_container_width=True)
               if but7:
                    st.session_state['kkk'] = 'Glucoss'
          with col8:
               but8=st.button('HbA1c', use_container_width=True)
               if but8:
                    st.session_state['kkk'] = 'HbA1c'

     with st.container():
          with col9:
               but9=st.button('WBC', use_container_width=True)
               if but9:
                    st.session_state['kkk'] = 'WBC'
          with col10:
               but10=st.button('RBC', use_container_width=True)
               if but10:
                    st.session_state['kkk'] = 'RBC'
          with col11:
               but11=st.button('HB', use_container_width=True)
               if but11:
                    st.session_state['kkk'] = 'HB'


     if st.session_state.kkk:
          st.subheader(f'👉 ' + st.session_state['kkk'] + '안내입니다', divider=True)
     else:
          st.session_state.kkk=''

     if '체질량지수'==st.session_state.kkk: 
          st.write('체질량지수(BMI : Body Mass Index)는 신장과 체중의 비율을 사용한 체중의 객관적인 지수를 말합니다.')
     if "혈압"==st.session_state.kkk: 
          st.write('성인의 정상적인 혈압 수치는 안정시 140/90mmHg로 유지되어야 합니다')
     if "색각"==st.session_state.kkk: 
          st.write('색각검사 안내')
     if "AST"==st.session_state.kkk: 
          st.write('간이 손상되면 혈액으로 빠져나와 혈중 농도가 올라가고 이 농도를 수치로 나타냅니다. 정상범위는 40 이하입니다')
          v = st.slider("❓ 검사결과지의 AST수치를 입력하세요", 0, 80, 40)
          if v == 0:
               st.write('') 
          elif v <= 40:
               st.write(f"AST수치 {v} : 🟢 정상입니다") 
          elif v > 40:
               st.write(f"AST수치 {v} : 🔴 이상입니다") 
     if "ALT"==st.session_state.kkk: 
          st.write('간염을 발견하기에 가장 효과적인 검사 항목 중 하나입니다. 정상범위는 41 이하입니다')
          v = st.slider("❓ 검사결과지의 ALT수치를 입력하세요", 0, 80, 41)
          if v == 0:
               st.write('') 
          elif v <= 41:
               st.write(f"ALT수치 {v} : 🟢 정상입니다") 
          elif v > 41:
               st.write(f"ALT수치 {v} : 🔴 이상입니다") 
     if "간염"==st.session_state.kkk:
          st.write('B형간염과 C형간염으로 나눠집니다. 정상범위는 음성입니다')
     if "Glucoss"==st.session_state.kkk:
          st.write('공복시 혈당수치입니다. 정상범위는 70~100 mg/dl입니다')
          v = st.slider("❓ 검사결과지의 Glucoss수치를 입력하세요", 0, 200, 100)
          if v == 0:
               st.write('') 
          elif v <= 100 and v >= 70:
               st.write(f"Glucoss수치 {v} : 🟢 정상입니다") 
          else:
               st.write(f"Glucoss수치 {v} : 🔴 이상입니다") 


with tab3:
     st.write('아래 링크를 누르시면 병무청 민원포털로 연결됩니다.')
     st.write('인증이 필요한 화면입니다.')
     st.link_button("건강검진 결과서 바로가기", "https://mwpt.mma.go.kr/caisBMHS/index_mwps.jsp?menuNo=22255")

     
st.divider()

#st.write("st.session_state 객체:", st.session_state)
