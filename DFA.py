import streamlit as st
import pandas as pd

dfa=pd.read_csv("戦力外.csv")
import scikitlearn
reg=setup(gpa,target="GPA")
st.write(reg)
