import streamlit as st
import pandas as pd

!pip install pycaret
dfa=pd.read_csv("戦力外.csv")
import pycaret
reg=setup(gpa,target="GPA")
st.write(reg)
