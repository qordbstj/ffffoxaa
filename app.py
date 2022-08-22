import streamlit as st
import pandas as pd
import numpy as np

data = pd.read_csv('기숙사수용현황분석.csv')
st.dataframe(data)
df = data[data['학교종류'] == '대학교']
num1 = len(df['학교'].unique())
num2 = len(df[df['설립구분'] != '사립']['학교'].unique())
num3 = len(df[df['설립구분'] == '사립']['학교'].unique())

col1, col2, col3 = st.columns(3)
st.metric(label="대학수", value=num1, delta="1.2 °F")
st.metric(label="국공립학교", value=num2, delta="1.2 °F")
st.metric(label="사립학교", value=num3, delta="1.2 °F")

st.write('기숙사현황')