import streamlit as st
import pandas as pd
dfa=pd.read_csv("戦力外.csv")
st.write(dfa.head())