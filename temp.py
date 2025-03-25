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

     if 'kkk' not in st.session_state:
          st.session_state['kkk'] = '체질량지수'

     if st.button('체질량지수', use_container_width=True):
          st.session_state['kkk'] = '체질량지수'
          st.rerun()
     if '체질량지수'==st.session_state.kkk: 
          st.subheader(f'👉 ' + st.session_state['kkk'] + '안내입니다', divider=True)
          st.write('체질량지수(BMI : Body Mass Index)는 신장과 체중의 비율을 사용한 체중의 객관적인 지수를 말합니다.')

     if st.button('혈압', use_container_width=True):
          st.session_state['kkk'] = '혈압'
          st.rerun()
     if "혈압"==st.session_state.kkk: 
          st.subheader(f'👉 ' + st.session_state['kkk'] + '안내입니다', divider=True)
          st.write('성인의 정상적인 혈압 수치는 안정시 140/90mmHg로 유지되어야 합니다')
          v1, v2 = st.slider("❓ 혈압수치의 이완기와 수축기 수치를 입력하세요", 40, 200, (90, 140))
          if v1 <= 90 and v2 <= 140:
               st.write(f"혈압  이완기({v1}), 수축기({v2}) : 🟢 정상입니다") 
          else:
               st.write(f"혈압  이완기({v1}), 수축기({v2}) : 🔴 이상입니다")

     if st.button('색각', use_container_width=True):
          st.session_state['kkk'] = '색각'
          st.rerun()
     if "색각"==st.session_state.kkk: 
          st.subheader(f'👉 ' + st.session_state['kkk'] + '안내입니다', divider=True)
          st.write('색각검사 안내')


     if st.button('AST', use_container_width=True):
          st.session_state['kkk'] = 'AST'
          st.rerun()
     if "AST"==st.session_state.kkk: 
          st.subheader(f'👉 ' + st.session_state['kkk'] + '안내입니다', divider=True)
          st.write('간이 손상되면 혈액으로 빠져나와 혈중 농도가 올라가고 이 농도를 수치로 나타냅니다. 정상범위는 40 이하입니다')
          v = st.slider("❓ 검사결과지의 AST수치를 입력하세요", 0, 80, 40)
          if v <= 40:
               st.write(f"AST수치 {v} : 🟢 정상입니다") 
          elif v > 40:
               st.write(f"AST수치 {v} : 🔴 이상입니다") 


     if st.button('ALT', use_container_width=True):
          st.session_state['kkk'] = 'ALT'
          st.rerun()
     if "ALT"==st.session_state.kkk: 
          st.subheader(f'👉 ' + st.session_state['kkk'] + '안내입니다', divider=True)
          st.write('간염을 발견하기에 가장 효과적인 검사 항목 중 하나입니다. 정상범위는 41 이하입니다')
          v = st.slider("❓ 검사결과지의 ALT수치를 입력하세요", 0, 80, 41)
          if v <= 41:
               st.write(f"ALT수치 {v} : 🟢 정상입니다") 
          elif v > 41:
               st.write(f"ALT수치 {v} : 🔴 이상입니다") 


     if st.button('간염', use_container_width=True):
          st.session_state['kkk'] = '간염'
          st.rerun()
     if "간염"==st.session_state.kkk:
          st.subheader(f'👉 ' + st.session_state['kkk'] + '안내입니다', divider=True)
          st.write('B형간염과 C형간염으로 나눠집니다. 정상범위는 음성입니다')


     if st.button('Glucoss', use_container_width=True):
          st.session_state['kkk'] = 'Glucoss'
          st.rerun()
     if "Glucoss"==st.session_state.kkk:
          st.subheader(f'👉 ' + st.session_state['kkk'] + '안내입니다', divider=True)
          st.write('공복시 혈당수치입니다. 정상범위는 70~100 mg/dl입니다')


     if st.button('HbA1c', use_container_width=True):
          st.session_state['kkk'] = 'HbA1c'
          st.rerun()
     if "HbA1c"==st.session_state.kkk:
          st.subheader(f'👉 ' + st.session_state['kkk'] + '안내입니다', divider=True)
          st.write('HbA1c')

     if st.button('WBC', use_container_width=True):
          st.session_state['kkk'] = 'WBC'
          st.rerun()
     if "WBC"==st.session_state.kkk:
          st.subheader(f'👉 ' + st.session_state['kkk'] + '안내입니다', divider=True)
          st.write('WBC(백혈구 수)가 정상 범위인지 확인합니다. 정상범위는 4.0~10.0 X 10³/μL입니다')


     if st.button('RBC', use_container_width=True):
          st.session_state['kkk'] = 'RBC'
          st.rerun()
     if "RBC"==st.session_state.kkk:
          st.subheader(f'👉 ' + st.session_state['kkk'] + '안내입니다', divider=True)
          st.write('RBC(적혈구 수)가 정상 범위인지 확인합니다. 정상범위는 4.2~6.3 X 10³/μL입니다')


     if st.button('HB', use_container_width=True):
          st.session_state['kkk'] = 'HB'
          st.rerun()
     if "HB"==st.session_state.kkk:
          st.subheader(f'👉 ' + st.session_state['kkk'] + '안내입니다', divider=True)
          st.write('Hb(Hemoglobin)은 혈액 속의 적혈구에 있는 단백질로, 혈색소라고도 합니다. 혈색소는 몸 전체에 산소를 운반하는 역할을 합니다. 혈색소 감소는 빈혈, 백혈병 등을 의심할 수 있습니다. 정상범위는 13.7~17.5g/㎗입니다')


     if st.session_state.kkk == False:
          st.session_state.kkk=''


with tab3:
     st.write('아래 링크를 누르시면 병무청 민원포털로 연결됩니다.')
     st.write('인증이 필요한 화면입니다.')
     st.link_button("건강검진 결과서 바로가기", "https://mwpt.mma.go.kr/caisBMHS/index_mwps.jsp?menuNo=22255")

     
st.divider()

#st.write("st.session_state 객체:", st.session_state)


import streamlit as st
import streamlit_analytics

with streamlit_analytics.track():
    st.text_input("Write something")
    st.button("Click me")
