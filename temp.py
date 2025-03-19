# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st

st.header('병역처분결과서의 결과를 확인하세요')

if st.button('현역입영대상'):
     st.write('1-3급은 현역입영대상입니다')
if st.button('사회복무요원소집대상'):
     st.write('4급은 사회복무요원 소집 대상입니다')