import streamlit as st
import pandas as pd
import numpy as np

data = pd.read_csv('기숙사수용현황분석.csv')
st.dataframe(data)

st.metric(label="대학수", value="70 °F", delta="1.2 °F")
st.metric(label="국공립학교", value="70 °F", delta="1.2 °F")
st.metric(label="사립학교", value="70 °F", delta="1.2 °F")

st.write('기숙사현황')