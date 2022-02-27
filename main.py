import streamlit as st
import pandas as pd
import yfinance as yf

st.title("Test")
variable = st.slider("Change")
df = yf.download("MSFT", period="100d")
print(df.head())

if st.checkbox("Show Raw Data"):
    st.subheader("Control Data")
    st.write(df)

st.subheader("Control Data Plotted")
st.line_chart(df.iloc[:, [False, False, False, True, False, False]])

