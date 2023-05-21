import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import os

st.set_page_config(layout="wide")
#st.title("เวชศาสตร์ฟื้นฟู กิจกรรมบำบัด")
#st.title("ศูนย์การแพทย์กาญจนาภิเษก")

st.write("## ข้อมูลคัดกรองภาพเอกซเรย์ปอด ตั้งแต่ปี 2023")

@st.cache_data(ttl=3600)
def load_data():
	df_froz =pd.read_csv("data_ck.csv", error_bad_lines=False)
	return df_froz

df_froz=load_data()
#num_shown=st.slider("จำนวนข้อมูลที่แสดง...",0,500,5)
#st.table(df_froz[:num_shown])

st.write(df_froz)