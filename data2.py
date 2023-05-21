import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.set_page_config(layout="centered")
st.title("ข้อมูลคัดกรองภาพเอกซเรย์ปอด ตั้งแต่ปี 2023")

#uploaded_file = st.file_uploader("Choose a file")
#if uploaded_file is not None:
df = pd.read_csv('checkup.csv',on_bad_lines='skip')
st.write(df)

  # Add some matplotlib code !
fig, ax = plt.subplots()
df.hist(
  bins=8,
  column="age",
  grid=False,
  figsize=(8, 8),
  color="#86bf91",
  zorder=2,
  rwidth=0.9,
  ax=ax,
)
st.write(fig)