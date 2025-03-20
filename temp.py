# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import numpy as np
import math
import random
from streamlit.runtime.scriptrunner import add_script_run_ctx, get_script_run_ctx
import time
from threading import Thread
import numpy as np

   
option = st.selectbox(
    '병역처분결과중 어떤 항목이 궁금하세요?',
    ('체질량지수','혈압','색각','AST','ALT','간염','Glucoss')
)
st.write('선택한 옵션:', option)


#from IPython.display import YouTubeVideo

st.header('병역처분결과서의 결과를 확인하세요')

if st.button('현역입영대상'):
     st.write('1-3급은 현역입영대상입니다')
if st.button('사회복무요원소집대상'):
     st.write('4급은 사회복무요원 소집 대상입니다')
if st.button('전시근로역'):
     st.write('5급은 전시근로역대상입니다')
if st.button('병역면제'):
     st.write('6급은 병역이 면제됩니다')
if st.button('재검대상'):
     st.write('7급 치유기간 이후에 다시 검사받으세요')
     
st.divider()
#st.title('this is title')
#st.header('this is header')
#st.subheader('this is subheader')

#video_SD = YouTubeVideo("jWQx2f-CErU?si=qycwg5gnqN0caB0_", width=500) # https://youtu.be/POe9SOEKotk
#display(video_SD)


import sqlite3
st.title("DB에 저장")

#데이터베이스 연결
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

#테이블생성(이미존재하면 생략)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS gsdatav (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        gshangmok TEXT NOT NULL,
        intro TEXT NOT NULL, 
        gsvalue1 TEXT,
        gsvalue2 TEXT,
        v1 TEXT,
        v2 TEXT,
        v3 TEXT,
        v4 TEXT,
        v5 TEXT
      )
''')

st.divider()

#사용자입력폼

st.subheader("사용자 정보 입력")
gshangmok = st.text_input("gshangmok")
intro = st.text_input("intro")
gsvalue1 = st.text_input("gsvalue1")
gsvalue2 = st.text_input("gsvalue2")

#데이터저장
#cursor.execute("INSERT INTO gsdatav(gshangmok, intro) VALUES ('체질량지수','체질량지수(BMI : Body Mass Index)란 신장과 체중의 비율을 사용한 체중의 객관적인 지수를 말합니다')")
#cursor.execute("INSERT INTO gsdatav(gshangmok, intro) VALUES ('색각','색각검사 안내')")
#cursor.execute("INSERT INTO gsdatav(gshangmok, intro) VALUES ('혈압','성인의 정상적인 혈압 수치는 안정시 140/90mmHg로 유지되어야 합니다')")
#cursor.execute("INSERT INTO gsdatav(gshangmok, intro) VALUES ('AST','간이 손상되면 혈액으로 빠져나와 혈중 농도가 올라가고 이 농도를 수치로 나타냅니다. 정상범위는 40 이하입니다')")
#cursor.execute("INSERT INTO gsdatav(gshangmok, intro) VALUES ('ALT','간염을 발견하기에 가장 효과적인 검사 항목 중 하나입니다. 정상범위는 40 이하입니다')")
#cursor.execute("INSERT INTO gsdatav(gshangmok, intro) VALUES ('간염','B형간염과 C형간염으로 나눠집니다. 정상범위는 음성입니다')")
#cursor.execute("INSERT INTO gsdatav(gshangmok, intro) VALUES ('Glucoss','공복시 혈당수치입니다. 정상범위는 70~100 mg/dl입니다')")
#conn.commit()

#데이터삽입 버튼
if st.button("수치내용저장"):
    if gshangmok and intro:
         cursor.execute("INSERT INTO gsdatav(gshangmok, intro) VALUES (?, ?)", (gshangmok, intro))
         conn.commit()
         st.success("Added successfully!")
    else :
        st.error("검사항목과 참고치설명은 필수입니다")

#데이터조회 및 출력
st.subheader("User Data from SQLite Database")
cursor.execute("SELECT * FROM gsdatav")
rows=cursor.fetchall()
df=pd.DataFrame(rows, columns=["id","gshangmok","intro"])
st.dataframe(df)

#연결종료
conn.close()

