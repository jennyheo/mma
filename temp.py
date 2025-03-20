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
    st.header ('병역처분결과중 어떤 항목이 궁금하세요?'),
    ('체질량지수','시력','혈압','색각','AST','ALT','간염','Glucoss')
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
    CREATE TABLE IF NOT EXISTS gsdata (
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

#데이터삽입 버튼
if st.button("수치내용저장"):
    if gshangmok and intro:
         cursor.execute("INSERT INTO gsdata(gshangmok, intro) VALUES (?, ?)", (gshangmok, intro))
         conn.commit()
         st.success("Added successfully!")
    else :
        st.error("검사항목과 참고치설명은 필수입니다")

#데이터조회 및 출력
st.subheader("User Data from SQLite Database")
cursor.execute("SELECT * FROM gsdata")
rows=cursor.fetchall()
df=pd.DataFrame(rows, columns=["id","gshangmok","intro","gsvalue1","gsvalue2"])
st.dataframe(df)

#연결종료
conn.close()

