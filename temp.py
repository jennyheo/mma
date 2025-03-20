# -*- codi     ng: utf-8 -*-

import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")

st.header('병역처분결과에 대해 알려드립니다')

with st.expander('😄 알려드립니다'):
  st.write('병역판정검사(입영판정검사) 결과지 내용에 대해 궁금한 사항을 안내합니다.')
  #st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

#사이드바 옵션
#st.sidebar.header('입력')
#user_name = st.sidebar.selectbox('병역처분 결과를 입력하세요', ['','현역입영대상','사회복무요원소집대상','전시근로역','병역면제','재검대상'])
#user_emoji = st.sidebar.selectbox('검사결과 중 어떤 항목이 궁금하신가요?', ['', '체질량지수','혈압','색각','AST','ALT','간염','Gloucoss'])
#user_food = st.sidebar.selectbox('가장 좋아하는 음식은?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

tab1, tab2 = st.tabs(['병역처분','검사참고치'])

with tab1:
     st.subheader('병역처분결과를 입력하세요', divider=True)
     #st.markdown("##### 병역처분결과를 입력하세요")
     #st.divider()
     user_name = st.selectbox('', ['','현역입영대상','사회복무요원소집대상','전시근로역','병역면제','재검대상'])


     if user_name != '':
          #st.subheader(', divider=True)
          st.markdown(f"#### 👈 {user_name} 안내입니다")
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
     #st.markdown("#### 검사결과 중 어떤 항목이 궁금하신가요?")
     #st.divider()

     user_emoji = st.selectbox('', ['', '체질량지수','혈압','색각','AST','ALT','간염','Glucoss'], )

     if user_emoji != '':
          st.subheader(f'👈 {user_emoji} 안내입니다', divider=True)
     else:
          st.subheader('')


     if user_emoji == '체질량지수' :
          st.write('체질량지수(BMI : Body Mass Index)는 신장과 체중의 비율을 사용한 체중의 객관적인 지수를 말합니다.')
     elif user_emoji == '색각' :
          st.write('색각검사 안내')
     elif user_emoji == '혈압' :
          st.write('성인의 정상적인 혈압 수치는 안정시 140/90mmHg로 유지되어야 합니다')
     elif user_emoji == 'AST' :
          st.write('간이 손상되면 혈액으로 빠져나와 혈중 농도가 올라가고 이 농도를 수치로 나타냅니다. 정상범위는 40 이하입니다')
     elif user_emoji == 'ALT' :
          st.write('간염을 발견하기에 가장 효과적인 검사 항목 중 하나입니다. 정상범위는 40 이하입니다')
     elif user_emoji == '간염' :
          st.write('B형간염과 C형간염으로 나눠집니다. 정상범위는 음성입니다')
     elif user_emoji == 'Glucoss' :
          st.write('공복시 혈당수치입니다. 정상범위는 70~100 mg/dl입니다')
     else: 
          st.write('')



#st.header("Two", divider=True)
#col1, col2, col3 = st.columns(3)

#with col1:
# if user_name != '':
    #st.write(f'{user_name} 안내입니다')
    #if {user_name} == '현역입영대상' :
        #st.write('1-3급은 현역입영대상입니다')
  #else:
    #st.write('👈  병역판정검사 처분결과를 선택하세요')

#with col2:
  #if user_emoji != '':
    #st.write(f'{user_emoji}는 당신이 좋아하는 **이모티콘**입니다!')
  #else:
    #st.write('👈 **이모티콘**을 선택해 주세요!')

     
st.divider()



