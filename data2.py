import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.set_page_config(layout="centered")
st.title("ข้อมูลคัดกรองภาพเอกซเรย์ปอด ตั้งแต่ปี 2023")

@st.cache_data(ttl=3600)
def load_data():
	df_froz =pd.read_csv("http://sigj.atwebpages.com/check/check2.csv", error_bad_lines=False)
	return df_froz

df_froz=load_data()
num_shown=st.slider("จำนวนข้อมูลที่แสดง...",0,500,5)
st.table(df_froz[:num_shown])
